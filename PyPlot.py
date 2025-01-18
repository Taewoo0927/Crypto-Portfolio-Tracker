import matplotlib.pyplot as plt
from datetime import datetime


class DataPlotter:
    """
    @brief A class inputs a dictionary. Example shown in example.json
    
    @Params json file.

    @Functions:
    Filter by attribute
    Print out list

    Example usage:
    @code
        plotter = DataPlotter()
        plotter.DataPlotter_insertData(dict)
        plotter.sort("Attribute_Name_1")
        plotter.line_plot()
    @endcode

    @note This class requires Matplotlib to be installed.
    """
    def __init__(self):
        self.potato = 1
        self.data = [];
    
    '''
    @brief 
    @params takes in a dictionary, and inserts into dataPlotter for future use
    '''
    def DataPlotter_insertData(self,data):
        self.data = data;
    
    '''
    @brief sorts, then plots by attribute of the self.graphdata data
    @params takes in a dictionary, and inserts into dataPlotter for future use
    '''
    def DataPlotter_deleteData(self,data):
        self.data = data;


    '''
    @brief sorts, then plots by attribute of the self.graphdata data
    @params: attribute wanted to sort
    '''
    def DataPlotter_plot(self,attribute):
        if attribute not in self.data:
            print(f"Error: '{attribute}' not found in data.")
            return
        
        timestamps = [item[0] for item in self.data[attribute]]  # Extract timestamps
        values = [item[1] for item in self.data[attribute]]  # Extract values

        # Convert UNIX timestamps (ms) to human-readable dates
        readable_dates = [datetime.fromtimestamp(ts / 1000).strftime('%Y-%m-%d %H:%M:%S') for ts in timestamps]

        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(readable_dates, values, marker='o', linestyle='-', label=attribute)
        plt.xlabel("Timestamp")
        plt.ylabel("Value")
        plt.title(f"{attribute.capitalize()} Over Time")
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    # Example data
    data = {
        "prices": [
            [1704067241331, 42261.0406175669],
            [1704070847420, 42493.2764087546],
            [1704074443652, 42654.0731066594]
        ],
        "market_caps": [
            [1704067241331, 827596236151.196],
            [1704070847420, 831531023621.411],
            [1704074443652, 835499399014.932]
        ],
        "total_volumes": [
            [1704067241331, 14305769170.9498],
            [1704070847420, 14130205376.1709],
            [1704074443652, 13697382902.2424]
        ]
    }

    # Create a DataPlotter instance
    plotter = DataPlotter()

    # Insert data into the plotter
    plotter.DataPlotter_insertData(data)

    # Plot 'prices' data
    plotter.DataPlotter_plot("prices")

    # Plot 'market_caps' data
    plotter.DataPlotter_plot("market_caps")

    # Plot 'total_volumes' data
    plotter.DataPlotter_plot("total_volumes")