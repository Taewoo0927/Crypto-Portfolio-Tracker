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
        plotter.sort("Attribute_Name_1")
        plotter.line_plot()
    @endcode

    @note This class requires Matplotlib to be installed.
    """
    def __init__(self):
        self.potato = 1
        self.graphdata = [];

    #@params 
    def DataPlotter_insertData(self,graphdata):
        self.graphdata = graphdata;
    
    def DataPlotter_sort(self):
        i=1;

if __name__ == "__main__":
    print("sandwhich")