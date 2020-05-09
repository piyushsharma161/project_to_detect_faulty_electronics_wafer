import pandas as pd

class Data_Getter:
    """
    This class shall  be used for obtaining the data from the source for training.

    Written By: Piyush
    Version: 1.0
    Revisions: None

    """
    def __init__(self, file_object, logger_object):
        self.training_file='Training_FileFromDB/InputFile.csv'
        self.file_object=file_object
        self.logger_object=logger_object

    def get_data(self):
        """
        Method Name: get_data
        Description: This method reads the data from source.
        Output: A pandas DataFrame.
        On Failure: Raise Exception

         Written By: Piyush
        Version: 1.0
        Revisions: None

        """
        self.logger_object.log(self.file_object,'Entered the get_data method of the Data_Getter class')
        try:
            self.data= pd.read_csv(self.training_file) # reading the data file
            self.data['Output'] = self.data['Output'].map({-1:0, 1:1})
            self.logger_object.log(self.file_object,'Data Load Successful.Exited the get_data method of the Data_Getter class')
            return self.data
        except Exception as e:
            self.logger_object.log(self.file_object,'Exception occured in get_data method of the Data_Getter class. Exception message: '+str(e))
            self.logger_object.log(self.file_object,
                                   'Data Load Unsuccessful.Exited the get_data method of the Data_Getter class')
            raise Exception()

if __name__ == "__main__":
    from application_logging import logger
    log_writer = logger.App_Logger()
    file_object = open("Training_Logs/ModelTrainingLog.txt", 'a+')
    dataload = Data_Getter(file_object, log_writer)
    data = dataload.get_data()

