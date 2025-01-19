
from datetime import datetime
import matplotlib.pyplot as plt

# DataPlotter.py
# This class is a widget in which, users can add graphs, sorted by an attribute, as well as 
# perform operations between different graphs. 
# Parry Zhuo
# data: Jan 17, 2025
class DataPlotter:
    """
    @brief A class inputs a dictionary. Example shown in example.json
    
    @Params json file.

    @Functions:
    Filter by attribute
    Print out list

    Example usage:
    @code

    @endcode

    @note This class requires Matplotlib to be installed.
    """
    def __init__(self):
        self.pyPlotDatabase = []
    '''
    @brief appends graph data into pyPlotDatabase.
    @params data: takes in a dictionary, and inserts into dataPlotter for future use
    @params nameOfCoin: name of coin to put on legend
    '''
    def DataPlotter_insertData(self,data,nameOfCoin):
        self.pyPlotDatabase.append([nameOfCoin,data])
    
    '''
    @brief sorts, then plots by attribute of the self.graphdata data
    @params takes in a dictionary, and inserts into dataPlotter for future use
    '''
    def DataPlotter_deleteData(self, nameOfCoin):
        """
        Removes a dataset identified by nameOfCoin from the pyPlotDatabase.

        @param nameOfCoin: The name of the dataset to remove.
        """
        for index, (name, _) in enumerate(self.pyPlotDatabase):
            if name == nameOfCoin:
                del self.pyPlotDatabase[index]
                print(f"Dataset '{nameOfCoin}' removed successfully.")
                return

        print(f"Dataset '{nameOfCoin}' not found.")
        
    '''
    @brief Plots data from pyPlotDatabase for a specific attribute.
    @params attribute: The key of the data to plot (e.g., "prices").
    '''
    def DataPlotter_plot_by_attribute(self, attribute):
        """
        Creates a Dear PyGui plot for a specific attribute from all datasets.
        """
        if not self.pyPlotDatabase:
            print("No data to plot.")
            return

        # Create a Dear PyGui window and plot
        with dpg.window(label="Data Plot", width=800, height=600):
            with dpg.plot(label=f"{attribute.capitalize()} Over Time", height=400, width=700):
                dpg.add_plot_legend()
                dpg.add_plot_axis(dpg.mvXAxis, label="Timestamp")
                y_axis = dpg.add_plot_axis(dpg.mvYAxis, label="Value")

                for name, data in self.pyPlotDatabase:
                    if attribute not in data:
                        print(f"Attribute '{attribute}' not found in dataset '{name}'.")
                        continue

                    # Extract timestamps and values
                    timestamps = [entry[0] / 1000 for entry in data[attribute]]  # Convert to seconds
                    values = [entry[1] for entry in data[attribute]]

                    # Add series to the plot
                    dpg.add_line_series(timestamps, values, label=name, parent=y_axis)


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


if __name__ == "__main__":
    # Create a DataPlotter instance
    data1 = {
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
    data2 = {
        "prices": [
            [1704067241331, 32261.0406175669],
            [1704070847420, 32493.2764087546],
            [1704074443652, 32654.0731066594]
        ],
        "market_caps": [
            [1704067241331, 727596236151.196],
            [1704070847420, 731531023621.411],
            [1704074443652, 735499399014.932]
        ],
        "total_volumes": [
            [1704067241331, 17305769170.9498],
            [1704070847420, 17130205376.1709],
            [1704074443652, 17697382902.2424]
        ]
    }

    dpg.create_context()
    plotter = DataPlotter()
    # Insert data into the plotter
    plotter.DataPlotter_insertData(data1, "Test1Table")
    plotter.DataPlotter_insertData(data2, "Test2Table")
    plotter.DataPlotter_insertData(data2, "Test3Table")
    # Plot all data in the database
    plotter.DataPlotter_plot_by_attribute("total_volumes")

    dpg.create_viewport(title='Dear PyGui Plot Example', width=900, height=700)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()