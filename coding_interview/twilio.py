import datetime
import json
import requests


def getUserTransaction(uid, txnType, monthYear):
    # Write your code here
    url = "https://jsonmock.hackerrank.com/api/transactions/search?userId={uid}&page={num}"
    transaction_data = requests.get(url.format(uid=uid,num=1))

    initial_data = json.loads(transaction_data.text)

    total_pages = initial_data["total_pages"]

    data = initial_data["data"]

    for page in range(2, total_pages + 1):
        page_response = requests.get(url.format(uid=uid, num=page))

        page_data = json.loads(page_response.text)["data"]

        data.extend(page_data)


    debit_amount = list(filter(lambda x: x["txnType"] == "debit" and datetime.datetime.strftime(datetime.datetime.fromtimestamp(x["timestamp"]/1000.0), "%m-%Y") == monthYear, data))

    total_spend = sum(list(map(lambda x: float("".join(x['amount'][1:].split(','))), debit_amount)))

    average_spend = total_spend/len(debit_amount)

    if txnType == "credit":
        credit_amount = list(filter(lambda x: x["txnType"] == "credit" and datetime.datetime.strftime(datetime.datetime.fromtimestamp(x["timestamp"]/1000.0), "%m-%Y") == monthYear, data))
        inter = list(map(lambda x: [x["id"] , float("".join(x['amount'][1:].split(',')))], credit_amount))
        final = list(filter(lambda x: x[1] > average_spend, inter))
    else:
        inter = list(map(lambda x: [x["id"] , float("".join(x['amount'][1:].split(',')))], debit_amount))
        final = list(filter(lambda x: x[1] > average_spend, inter))

    if final:
        return sorted(list(map(lambda x: x[0], final)))
    return -1


    print(data)

getUserTransaction(4, 'debit', '02-2019')