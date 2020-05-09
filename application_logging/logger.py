from datetime import datetime


class App_Logger:
    def __init__(self):
        pass

    def log(self, file_object, log_message):
        self.now = datetime.now()
        self.date = self.now.date()
        self.current_time = self.now.strftime("%H:%M:%S")
        file_object.write(
            str(self.date) + "/" + str(self.current_time) + "\t\t" + log_message +"\n")


if __name__ == "__main__":
    log_file = open('C:/projects/WaferFaultDetection1/testlogging.txt', 'a+')
    app1 = App_Logger()
    app1.log(log_file,'test successfull')

