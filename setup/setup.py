from datetime import date, timedelta

import requests


def save_data_in_file(requested_date):
    r = requests.get(f"https://portal.amfiindia.com/DownloadNAVHistoryReport_Po.aspx?frmdt={requested_date}")
    print(r.status_code)
    f = open(f"data/{requested_date}.csv", "a")
    f.write(str(r.content, 'utf-8'))
    f.close()


# access publicly available data from AMF https://www.amfiindia.com/net-asset-value/nav-history
def collect_data():
    start_date = date(year=2006, month=4, day=1)  # data inception date at AMF
    end_date = date.today()
    delta = end_date - start_date

    for request_date in range(delta.days + 1):
        day = start_date + timedelta(days=request_date)
        print(day.strftime("%d-%b-%Y"))
        save_data_in_file(day.strftime("%d-%b-%Y"))


if __name__ == '__main__':
    collect_data()
