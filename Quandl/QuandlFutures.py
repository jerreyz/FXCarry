import quandl as quandl
quandl.ApiConfig.api_key = 'FoJiz-sscd-YSNKZZ4P3'
locationCSVConfig = "%s\%s" %(os.getcwd(),'QuandlFuturesConfig.csv')



class QuandlFuturesContract(object):
    """
    An individual futures contract, with additional Quandl methods
    """ def __init__(self, quandlCode,dateOfContract):
        try:
            # 1. Parse a string to datetime
            datestamp   = pd.to_datetime(dateOfContract,format='%Y%m')
        except:
            raise ValueError("Need a YYYYMM format ")

        # 3. Read in the Config file    
        self.QuandlCSV = pd.read_csv(locationCSVConfig).set_index("QCODE")
        self.quandlCode = quandlCode
        # 4. Futures contract list in letters, How months are defined in Futures trading, weird I know
        MONTH_LIST = ["F", "G", "H", "J", "K", "M", "N", "Q", "U", "V", "X", "Z"]
        # 5 Get the correct month letter and concatenate it with the year
        quandl_date_id  = MONTH_LIST[datestamp.month-1] + str(datestamp.year)

        # 6. Concatenate the market code and quandl date id to get the timeseries id
        self.quandlIdentifier = "%s/%s%s" % (cls.QuandlCSV.loc[quandlCode,"MARKET"],quandlCode,quandl_date_id )
   

      
    
    def get_quandl_identifier(self):
        return self.quandlIdentifier

    def get_pysystemtradecode_for_instrument(self):

        return self.QuandlCSV.loc[self.quandlCode,'CODE']
    def get_quandlmarket_for_instrument(self):

        return self.QuandlCSV.loc[self.quandlCode,'MARKET']

    def get_start_date_of_firstcontract(self):

        return self.QuandlCSV.loc[self.quandlCode,'FIRST_CONTRACT']

    def get_dividing_factor(self):

        return  self.QuandlCSV.loc[self.quandlCode,'FACTOR']
    
    
    
