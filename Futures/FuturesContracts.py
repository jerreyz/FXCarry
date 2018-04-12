class futuresInstrument(object):
    """
    Define a generic instrument
    """

    def __init__(self, instrument_code,  **kwargs):

        assert type(instrument_code) is str

        self.instrument_code = instrument_code

        ## any remaining data we dump into a meta data dict
        self.meta_data = kwargs

        self._isempty = False

    def __repr__(self):
        return self.instrument_code

    def as_dict(self):

        if self.empty():
            raise Exception("Can't create dict from empty object")

        dict_of_values = self.meta_data
        dict_of_values['instrument_code'] = self.instrument_code
        return dict_of_values


    @classmethod
    def create_from_dict(futuresInstrument, dict_of_values):

        instrument_code = dict_of_values.pop('instrument_code')

        return futuresInstrument(instrument_code, **dict_of_values)

    @classmethod
    def create_empty(futuresInstrument):
        futures_instrument = futuresInstrument("")
        futures_instrument._isempty = True

        return futures_instrument

    def empty(self):
        return self._isempty


class futuresContract(object):
    """
    Define an individual futures contract
    This is a combination of an instrument_object and contract_date object
    """
    def __init__(self, instrument_object, contract_date_object):
        """
        :param instrument_object:
        :param contract_date_object: contractDate or contractDateWithRollParameters
        """

        self.instrument = instrument_object
        self.contract_date = contract_date_object
        self._is_empty = False


    def __repr__(self):
        return self.ident()

    @classmethod
    def create_empty(futuresContract):
        fake_instrument = futuresInstrument("EMPTY")
        fake_contract_date = contractDate("150001")

        futures_contract = futuresContract(fake_instrument, fake_contract_date)
        futures_contract._is_empty = True

        return futures_contract

    def empty(self):
        return self._is_empty

    def ident(self):
        return self.instrument_code + "/"+ self.date

    def as_tuple(self):
        return self.instrument_code, self.date

    def as_dict(self):
        """
        Turn into a dict. We only include instrument_code from the instrument_object, the rest would be found elsewhere
           plus we have all the results from as_dict on the contract_date
        :return: dict
        """

        if self.empty():
            raise Exception("Can't create dict from empty object")

        contract_date_dict = self.contract_date.as_dict()
        contract_date_dict['instrument_code'] = self.instrument_code

        return contract_date_dict

    @classmethod
    def create_from_dict_with_instrument_dict(futuresContract, instrument_dict, futures_contract_dict):
        """
        :param instrument_dict: The result of running .as_dict on a futuresInstrument
        :param futures_contract_dict: The result of running .as_dict on a futuresContract.
        :return: futuresContract object
        """

        # If we run as_dict on a futuresContract we get the instrument_code
        assert instrument_dict['instrument_code'] == futures_contract_dict['instrument_code']

        contract_date_dict = copy(futures_contract_dict)
        contract_date_dict.pop('instrument_code') # not used

        contract_date_object = contractDate.create_from_dict(contract_date_dict)
        instrument_object = futuresInstrument.create_from_dict(instrument_dict)

        return futuresContract(instrument_object, contract_date_object)

    @classmethod
    def create_from_dict(futuresContract, futures_contract_dict):
        """
        :param futures_contract_dict: The result of running .as_dict on a futuresContract.
        :return: futuresContract object
        """

        contract_date_dict = copy(futures_contract_dict)
        instrument_code = contract_date_dict.pop('instrument_code')

        # We just do a 'bare' instrument with only a code
        instrument_dict = dict(instrument_code = instrument_code)

        contract_date_object = contractDate.create_from_dict(contract_date_dict)
        instrument_object = futuresInstrument.create_from_dict(instrument_dict)

        return futuresContract(instrument_object, contract_date_object)

    @classmethod
    def create_from_dict_with_rolldata(futuresContract, futures_contract_dict, roll_data_dict):
        """
        :param futures_contract_dict: The result of running .as_dict on a futuresContract.
        :param roll_data_dict: A roll data dict
        :return: futuresContract object
        """

        contract_date_dict = copy(futures_contract_dict)
        instrument_code = contract_date_dict.pop('instrument_code')

        # We just do a 'bare' instrument with only a code
        instrument_dict = dict(instrument_code = instrument_code)

        contract_date_with_rolldata_object = contractDateWithRollParameters.create_from_dict(contract_date_dict, roll_data_dict)
        instrument_object = futuresInstrument.create_from_dict(instrument_dict)

        return futuresContract(instrument_object, contract_date_with_rolldata_object)


    @classmethod
    def simple(futuresContract, instrument_code, contract_date, **kwargs):

        return futuresContract(futuresInstrument(instrument_code), contractDate(contract_date, **kwargs))


    @classmethod
    def identGivenCodeAndContractDate(futuresContract, instrument_code, contract_date):
        """
        Return an identification given a code and contract date
        :param instrument_code: str
        :param contract_date: str, following contract date rules
        :return: str
        """

        futures_contract = futuresContract.simple(instrument_code, contract_date)

        return futures_contract.ident()

    @property
    def instrument_code(self):
        return self.instrument.instrument_code

    @property
    def date(self):
        return self.contract_date.contract_date

    @property
    def expiry_date(self):
        return self.contract_date.expiry_date

    @classmethod
    def approx_first_held_futuresContract_at_date(futuresContract, instrument_object, roll_parameters, reference_date):
        try:
            first_contract_date = roll_parameters.approx_first_held_contractDate_at_date(reference_date)
        except AttributeError:
            raise Exception("You can only do this if contract_date_object is contractDateWithRollParameters")

        return futuresContract(instrument_object, first_contract_date)

    @classmethod
    def approx_first_priced_futuresContract_at_date(futuresContract, instrument_object, roll_parameters, reference_date):
        try:
            first_contract_date = roll_parameters.approx_first_priced_contractDate_at_date(reference_date)
        except AttributeError:
            raise Exception("You can only do this if contract_date_object is contractDateWithRollParameters")

        return futuresContract(instrument_object, first_contract_date)


    def next_priced_contract(self):
        try:
            next_contract_date = self.contract_date.next_priced_contract()
        except AttributeError:
            raise Exception("You can only do this if contract_date_object is contractDateWithRollParameters")

        return futuresContract(self.instrument, next_contract_date)


    def previous_priced_contract(self):

        try:
            previous_contract_date = self.contract_date.previous_priced_contract()
        except AttributeError:
            raise Exception("You can only do this if contract_date_object is contractDateWithRollParameters")

        return futuresContract(self.instrument, previous_contract_date)

    def carry_contract(self):

        try:
            carry_contract = self.contract_date.carry_contract()
        except AttributeError:
            raise Exception("You can only do this if contract_date_object is contractDateWithRollParameters")

        return futuresContract(self.instrument, carry_contract)

    def next_held_contract(self):
        try:
            next_held_date = self.contract_date.next_held_contract()
        except AttributeError:
            raise Exception("You can only do this if contract_date_object is contractDateWithRollParameters")

        return futuresContract(self.instrument, next_held_date)

    def previous_held_contract(self):
        try:
            previous_held_date = self.contract_date.previous_held_contract()
        except AttributeError:
            raise Exception("You can only do this if contract_date_object is contractDateWithRollParameters")

        return futuresContract(self.instrument, previous_held_date)









class quandlFuturesContract(futuresContract):
    """
    An individual futures contract, with additional Quandl methods
    """

    def __init__(self, futures_contract, quandl_instrument_data = USE_DEFAULT):
        """
        We always create a quandl contract from an existing, normal, contract
        :param futures_contract: of type FuturesContract
        """

        super().__init__(futures_contract.instrument, futures_contract.contract_date)

        if quandl_instrument_data is USE_DEFAULT:
            quandl_instrument_data = quandlFuturesConfiguration()

        self._quandl_instrument_data = quandl_instrument_data

    def quandl_identifier(self):
        """
        Returns the Quandl identifier for a given contract
        :return: str
        """

        quandl_year = str(self.contract_date.year())
        quandl_month = self.contract_date.letter_month()

        try:
            quandl_date_id = quandl_month + quandl_year

            market = self.get_quandlmarket_for_instrument()
            codename = self.get_quandlcode_for_instrument()

            quandldef = '%s/%s%s' % (market, codename, quandl_date_id)

            return quandldef
        except:
            raise ValueError("Can't turn %s %s into a Quandl Contract" % (self.instrument_code, self.contract_date))

    def get_quandlcode_for_instrument(self):

        return self._quandl_instrument_data.get_quandlcode_for_instrument(self.instrument_code)

    def get_quandlmarket_for_instrument(self):

        return self._quandl_instrument_data.get_quandlmarket_for_instrument(self.instrument_code)

    def get_start_date(self):

        return self._quandl_instrument_data.get_start_date(self.instrument_code)

    def get_dividing_factor(self):

        return self._quandl_instrument_data.get_quandl_dividing_factor(self.instrument_code)


    def get_quandl_dividing_factor(self, instrument_code):

        config = self.get_instrument_config(instrument_code)
        factor = config.FACTOR

        return float(factor)
