class DataPlotter:
    """
    @brief A class for creating and managing plots using Matplotlib's PyPlot.

    @Params
    attributes - this is signified, 

    @Functions:

    Change parameters,
    Print out list

    @ Questions or observations:

    The data required by the GUI will be returned, no GUI will be implemented in this class
    Input will not interact with GUI either, it expects DICTIONARY.      
    TBH, is class even needed for such a task?
    
    Example usage:
    @code
        plotter = DataPlotter()
        plotter.line_plot([1, 2, 3], [4, 5, 6], title="Example Plot", xlabel="Time", ylabel="Value")
    @endcode

    @note This class requires Matplotlib to be installed.
    """
    def __init__(self, attributes):
        self.potato = 1

if __name__ == "__main__":
    print("sandwhich")