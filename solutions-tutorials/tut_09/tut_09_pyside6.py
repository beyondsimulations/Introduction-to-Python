import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                              QLabel, QLineEdit, QPushButton, QGridLayout, QHBoxLayout,
                              QFrame)
from PySide6.QtCore import Qt
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class ModernFrame(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                padding: 20px;
            }
        """)
        self.setObjectName("modernFrame")

class InvestmentCalculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Investment Calculator")
        self.setMinimumSize(1000, 600)

        # Set the main window style
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f0f2f5;
            }
            QLabel {
                font-size: 14px;
                color: #2c3e50;
                font-weight: 500;
            }
            QLineEdit {
                padding: 8px;
                border: 2px solid #e0e0e0;
                border-radius: 5px;
                background-color: white;
                font-size: 14px;
                min-width: 200px;
            }
            QLineEdit:focus {
                border: 2px solid #3498db;
            }
            QPushButton {
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 14px;
                font-weight: bold;
                min-width: 100px;
            }
            QPushButton#calculateBtn {
                background-color: #3498db;
                color: white;
                border: none;
            }
            QPushButton#calculateBtn:hover {
                background-color: #2980b9;
            }
            QPushButton#resetBtn {
                background-color: #e74c3c;
                color: white;
                border: none;
            }
            QPushButton#resetBtn:hover {
                background-color: #c0392b;
            }
            QLabel#resultLabel {
                font-size: 18px;
                font-weight: bold;
                color: #2c3e50;
                padding: 10px;
            }
        """)

        # Create central widget and main layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(20, 20, 20, 20)

        # Create left panel with modern frame
        left_frame = ModernFrame()
        left_layout = QVBoxLayout(left_frame)
        main_layout.addWidget(left_frame)

        # Add title to left panel
        title_label = QLabel("Investment Calculator")
        title_label.setStyleSheet("""
            font-size: 24px;
            font-weight: bold;
            color: #2c3e50;
            margin-bottom: 20px;
        """)
        left_layout.addWidget(title_label)

        # Create input fields container
        input_widget = QWidget()
        layout = QGridLayout(input_widget)
        layout.setSpacing(15)
        left_layout.addWidget(input_widget)

        # Create input fields with modern styling
        self.initial = QLineEdit()
        self.annual = QLineEdit()
        self.rate = QLineEdit()
        self.years = QLineEdit()

        # Add input fields with labels
        layout.addWidget(QLabel("Initial Investment (€):"), 0, 0)
        layout.addWidget(self.initial, 0, 1)
        layout.addWidget(QLabel("Annual Contribution (€):"), 1, 0)
        layout.addWidget(self.annual, 1, 1)
        layout.addWidget(QLabel("Expected Return Rate (%):"), 2, 0)
        layout.addWidget(self.rate, 2, 1)
        layout.addWidget(QLabel("Investment Period (years):"), 3, 0)
        layout.addWidget(self.years, 3, 1)

        # Create buttons with modern styling
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)

        calc_button = QPushButton("Calculate")
        calc_button.setObjectName("calculateBtn")
        calc_button.clicked.connect(self.calculate)

        reset_button = QPushButton("Reset")
        reset_button.setObjectName("resetBtn")
        reset_button.clicked.connect(self.reset)

        button_layout.addWidget(calc_button)
        button_layout.addWidget(reset_button)
        button_layout.addStretch()

        left_layout.addLayout(button_layout)

        # Create result label
        self.result_label = QLabel()
        self.result_label.setObjectName("resultLabel")
        self.result_label.setAlignment(Qt.AlignCenter)
        left_layout.addWidget(self.result_label)

        left_layout.addStretch()

        # Create right panel for graph with modern frame
        right_frame = ModernFrame()
        graph_layout = QVBoxLayout(right_frame)
        main_layout.addWidget(right_frame)

        # Create matplotlib figure with modern style
        self.figure, self.ax = plt.subplots()
        self.figure.set_facecolor('white')
        self.ax.set_facecolor('white')
        self.canvas = FigureCanvas(self.figure)
        graph_layout.addWidget(self.canvas)

        # Set default values
        self.reset()

    def reset(self):
        """Reset all input fields to default values"""
        self.initial.setText("10000")
        self.annual.setText("1200")
        self.rate.setText("7")
        self.years.setText("10")
        self.result_label.setText("")
        self.ax.clear()
        self.canvas.draw()

    def calculate(self):
        try:
            initial = float(self.initial.text())
            annual = float(self.annual.text())
            rate = float(self.rate.text()) / 100
            years = int(self.years.text())

            # Calculate year-by-year values
            values = [initial]
            for _ in range(years):
                values.append((values[-1] + annual) * (1 + rate))

            # Display final result
            self.result_label.setText(
                f"Future Value: €{values[-1]:,.2f}"
            )

            # Update graph
            self.ax.clear()
            years_list = list(range(years + 1))

            # Plot with modern colors
            self.ax.plot(years_list, values, color='#3498db', linewidth=3, label='Investment Value')
            contributions = [initial + annual * year for year in years_list]
            self.ax.plot(years_list, contributions, color='#e74c3c', linewidth=2,
                        linestyle='--', label='Contributions')

            # Customize the graph
            self.ax.set_xlabel('Years', fontsize=10, color='#2c3e50')
            self.ax.set_ylabel('Value (€)', fontsize=10, color='#2c3e50')
            self.ax.set_title('Investment Growth Over Time', fontsize=12,
                            color='#2c3e50', pad=20)
            self.ax.grid(True, linestyle='--', alpha=0.7)
            self.ax.legend(frameon=True, fancybox=True, shadow=True)

            # Format y-axis
            self.ax.yaxis.set_major_formatter(
                plt.FuncFormatter(lambda x, p: f'€{x:,.0f}')
            )

            # Update the graph
            self.figure.tight_layout()
            self.canvas.draw()

        except ValueError:
            self.result_label.setText("Please enter valid numbers")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = InvestmentCalculator()
    window.show()
    sys.exit(app.exec())
