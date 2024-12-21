import numpy as np
import matplotlib.pyplot as plt

def generate_holiday_data():
    holidays = ['New Year', 'Easter', 'Diwali', 'Christmas', 'Independence Day']
    costs = np.random.randint(100, 1000, size=len(holidays))  
    days = np.random.randint(0, 7, size=len(holidays))  
    return holidays, costs, days

def calculate_average_cost(costs):
    return np.mean(costs)

def plot_holiday_data(holidays, costs, days):
    day_labels = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    days_str = [day_labels[day] for day in days]

    plt.figure(figsize=(10, 5))
    plt.bar(holidays, costs, color='skyblue', alpha=0.8)
    for i, cost in enumerate(costs):
        plt.text(i, cost + 20, f"${cost}", ha='center', fontsize=10)
    plt.title("Holiday Costs")
    plt.xlabel("Holidays")
    plt.ylabel("Cost (in $)")
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    unique_days, day_counts = np.unique(days_str, return_counts=True)
    plt.figure(figsize=(6, 6))
    plt.pie(day_counts, labels=unique_days, autopct='%1.1f%%', colors=plt.cm.Paired.colors)
    plt.title("Holidays by Day of the Week")

    plt.show()

def main():
    holidays, costs, days = generate_holiday_data()

    avg_cost = calculate_average_cost(costs)
    print(f"Average holiday cost: ${avg_cost:.2f}")

    # Plot holiday data
    plot_holiday_data(holidays, costs, days)

if __name__ == "__main__":
    main()
