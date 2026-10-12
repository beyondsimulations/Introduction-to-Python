"""Check that an exported marimo notebook keeps its work across a reload.

    uv run python helpers/check_reload.py _site/notebooks/nb_04_lab_menu
    uv run python helpers/check_reload.py <export dir> --browser firefox

Types a marker into the first code cell, presses nothing else, reloads, and looks
for the marker. It only survives if autosave wrote the notebook and the script that
helpers/export_marimo.py injects handed it back, so one assert covers both patches.
A new tab on the same address must start clean. Exit 1 on failure.

Needs playwright: uv add --dev playwright && uv run playwright install chromium
"""
import argparse
import functools
import http.server
import sys
import threading
from pathlib import Path

MARKER = "# reload-check-4711"
CELLS = '.cm-content[data-language="python"]'


class _Handler(http.server.SimpleHTTPRequestHandler):
    protocol_version = "HTTP/1.1"  # HTTP/1.0 drops marimo's ~700 asset requests

    def log_message(self, *args):
        pass


def wait_for_cells(page):
    page.wait_for_selector(f"{CELLS} >> visible=true", timeout=180_000)
    page.wait_for_timeout(8_000)  # let pyodide start and the cells run


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("export_dir", type=Path)
    parser.add_argument("--browser", default="chromium", choices=["chromium", "firefox", "webkit"])
    args = parser.parse_args()
    export_dir = args.export_dir.resolve()
    # Labs load ../assets/, so serve the parent folder when the bundle is shared.
    root = export_dir if (export_dir / "assets").is_dir() else export_dir.parent
    path = "" if root == export_dir else f"{export_dir.name}/"
    httpd = http.server.ThreadingHTTPServer(("127.0.0.1", 0), functools.partial(_Handler, directory=str(root)))
    threading.Thread(target=httpd.serve_forever, daemon=True).start()
    url = f"http://127.0.0.1:{httpd.server_address[1]}/{path}"

    from playwright.sync_api import sync_playwright

    with sync_playwright() as pw:
        browser = getattr(pw, args.browser).launch()
        context = browser.new_context()
        page = context.new_page()
        page.goto(url)
        wait_for_cells(page)
        cell = page.locator(f"{CELLS} >> visible=true").first
        cell.click()
        page.keyboard.press("ControlOrMeta+End")
        page.keyboard.type("\n" + MARKER, delay=10)
        page.wait_for_timeout(4_000)  # autosave fires one second after typing stops
        page.reload()
        wait_for_cells(page)
        kept = page.locator(CELLS, has_text=MARKER).count() > 0
        fresh = context.new_page()
        fresh.goto(url)
        wait_for_cells(fresh)
        clean = fresh.locator(CELLS, has_text=MARKER).count() == 0
        browser.close()
    httpd.shutdown()

    print(f"{'ok  ' if kept and clean else 'FAIL'} {export_dir.name} ({args.browser}): "
          f"work kept after reload: {kept}, new tab starts clean: {clean}")
    return 0 if kept and clean else 1


if __name__ == "__main__":
    sys.exit(main())
