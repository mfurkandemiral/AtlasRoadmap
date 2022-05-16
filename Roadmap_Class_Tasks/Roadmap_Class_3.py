import datetime


class WebPush:
    def __init__(self, platform, optin: bool, global_frequency_capping, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        print(self.push_type + " Push gönderildi!")

    def get_push_info(self, private_variable):
        return self.platform, self.optin, self.global_frequency_capping, self.start_date, \
               self.end_date, self.language, self.push_type, private_variable


class TriggerPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 trigger_page: str):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.trigger_page = trigger_page


class BulkPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 send_date: int):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.send_date = send_date


class SegmentPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 segment_name: str):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.segment_name = segment_name


class PriceAlertPush(WebPush):
    def discountPrice(self, price_info: int, discount_rate: float):
        return price_info * discount_rate


class InStockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 stock_info: bool):
        super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)

        self.stock_info = stock_info

    def stockUpdate(self):
        self.stock_info = not self.stock_info

        return self.stock_info


TriggerPushType = TriggerPush("Mobile", True, 25, datetime.datetime(2022, 1, 1).strftime("%m/%d/%Y"),
                              datetime.datetime(2022, 2, 1).strftime("%m/%d/%Y"), "tr_TR", "Trigger", "HomePage")
TriggerPushType.send_push()
print(TriggerPushType.get_push_info(TriggerPushType.trigger_page), "\n")

BulkPushType = BulkPush("Desktop", True, 20, datetime.datetime(2022, 2, 1).strftime("%m/%d/%Y"),
                        datetime.datetime(2022, 3, 1).strftime("%m/%d/%Y"), "en_GB", "Bulk", 5)
BulkPushType.send_push()
print(BulkPushType.get_push_info(BulkPushType.send_date), "\n")

SegmentPushType = SegmentPush("Tablet", True, 15, datetime.datetime(2022, 3, 1).strftime("%m/%d/%Y"),
                              datetime.datetime(2022, 4, 1).strftime("%m/%d/%Y"), "fr_FR", "Segment", "Segment")
SegmentPushType.send_push()
print(SegmentPushType.get_push_info(SegmentPushType.segment_name), "\n")

PriceAlertPushType = PriceAlertPush("Mobile", True, 10, datetime.datetime(2022, 4, 1).strftime("%m/%d/%Y"),
                                    datetime.datetime(2022, 5, 1).strftime("%m/%d/%Y"), "de-DE", "Price Alert")
PriceAlertPushType.send_push()
print(PriceAlertPushType.get_push_info(PriceAlertPushType.discountPrice(200, 0.1)))
print("SEPETTE {} TL İNDİRİM İÇİN SON GÜN!".format(PriceAlertPushType.discountPrice(200, 0.1)), "\n")

InStockPushType = InStockPush("Desktop", True, 10, datetime.datetime(2022, 5, 1).strftime("%m/%d/%Y"),
                              datetime.datetime(2022, 6, 1).strftime("%m/%d/%Y"), "tr_TR", "InStock", True)

InStockPushType.send_push()
print(InStockPushType.get_push_info(InStockPushType.stock_info))
print("Stock Status : {} ".format(InStockPushType.stockUpdate()))