# Holiday Analysis with Python

This project showcases how to analyze and visualize holiday-related data using Python. It leverages powerful libraries like **NumPy**, **Matplotlib**, and user-defined functions to provide insights into holiday costs and their distribution across the days of the week.

---

## Features
- Generate random holiday data, including names, costs, and days of the week.
- Calculate average holiday costs.
- Visualize data using:
  - A bar chart for holiday costs.
  - A pie chart for the distribution of holidays across the days of the week.

---

## Installation
1. Clone this repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd Python Projects
   ```
3. Install the required dependencies:
   ```bash
   pip install numpy matplotlib
   ```

---

## Usage
1. Run the script:
   ```bash
   python holiday_analysis.py
   ```
2. View the output in your terminal and the visualizations generated in a pop-up window.

---

## Code Structure
### Functions
- **`generate_holiday_data()`**: Generates mock data for holidays, including names, costs, and days of the week.
- **`calculate_average_cost(costs)`**: Computes the average holiday cost from the dataset.
- **`plot_holiday_data(holidays, costs, days)`**: Visualizes the data using bar and pie charts.

### Libraries Used
- **NumPy**: For numerical operations and random data generation.
- **Matplotlib**: For creating visualizations.

---

## Example Output
### Bar Chart: Holiday Costs
![Holiday Costs Bar Chart](images/holiday_costs.png)

### Pie Chart: Holiday Days of the Week
![Holiday Days Pie Chart](images/holiday_days.png)

---

## Customization
- Modify the list of holidays in `generate_holiday_data()` to include your favorite holidays.
- Adjust the cost range in `np.random.randint()` to match your analysis needs.

---

## Contributing
Contributions are welcome! Feel free to open an issue or submit a pull request.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contact
For any questions or feedback, feel free to reach out via LinkedIn or email.
