class QuandlFutures(object):

     # This class deals with handling quandl futures
     
    def __init__(self):
        #The config file will be a stored csv in the future, it holds all instruments we would like to get from quandl.
        
        self.config_data =pd.DataFrame({'CODE':'EDOLLAR','QCODE':'ED','FACTOR':1,'MARKET':'CME','FIRST_CONTRACT':198203},index=[0]).set_index('CODE')
        
    def get_list_of_instruments(self):
        # this method returns all the instruments we can get
        
        return list(self.config_data.index)
        
    def get_instrument_config(self, instrument_code):
    
        # This method will try to get all the information on a specific instrument
        if instrument_code not in self.get_list_of_instruments():
            raise Exception("Instrument %s missing from config file " % (instrument_code))
          
        instrumentconfigdata = self.config_data.loc[instrument_code]
        return instrumentconfigdata
        
    def get_quandl_code_for_instrument(self,instrument):
     
     # Gets the QUANDL code for a specific instrument
        return self.config_data.loc[instrument,'QCODE']
