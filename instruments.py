from tinkoff.invest import Instrument, InstrumentIdType, Client

from tokens import TOKENS

CURRENCY_FIGIS = {
    'usd': 'BBG0013HGFT4',
    'eur': 'BBG0013HJJ31',
    'cny': 'BBG0013HRTL0',
    'hkd': 'BBG0013HSW87',
    'xau': 'BBG000VJ5YR4'
}

DOLLAR_FIGI = CURRENCY_FIGIS['usd']

class Instruments:
    cache = dict()
    client = None

    @staticmethod
    def get(figi: str) -> Instrument:
        if Instruments.client is None:
            Instruments.client = Client(TOKENS[0]).__enter__()
        if figi not in Instruments.cache:
            Instruments.cache[figi] = \
                (Instruments.client.instruments.get_instrument_by(
                    id_type=InstrumentIdType.INSTRUMENT_ID_TYPE_FIGI, id=figi
                ).instrument)
        return Instruments.cache[figi]

