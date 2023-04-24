from cryptos import * #for private key, public key and bitcoin address generation
import requests #for web requests
import time #for our pause of 1 second to respect the blockchain api
import csv #for a csv file we will write results to

#setup
BTC_API_ENDPOINT = 'https://blockchain.info/q/addressbalance/' #1 request every 10 seconds
fileInput = "quotes.txt" #file you want to read quotes in from
fileOutput = "result.csv" #output csv file
header = ['Quotation', 'Address', 'Balance'] #top row header for CSV file

#Write header row to the file
with open(fileOutput, 'w', newline='') as fileHeader:
    writer = csv.writer(fileHeader)
    writer.writerow(header)
    fileHeader.close()

#balance checker
def check_balance(address):
    url = BTC_API_ENDPOINT + address
    response = requests.get(url)
    if response.status_code == 200:
        balance = float(response.text) / 100000000  # convert satoshis to BTC
        return balance
    else:
        print(f'Error checking balance for address {address}: {response.text}')
        return None

#bitcoin brainwallet address generator
def bitcoinWalletGenerator(myQuote):
    
    #generate the private key
    Private_Key = sha256(myQuote)
    b = Bitcoin()
    #generate the public key
    bitCoinAddress = b.privtoaddr(Private_Key)
    
    return bitCoinAddress

#countdown timer for queries
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        time_sec -= 1

def testQuote(theQuote):
    #for each quote in quotes generate an address

    address = bitcoinWalletGenerator(theQuote)
    #check the balanace of the address
    balance = check_balance(address) #only 1 request every 10 seconds to respect the API
    print('Current Quote: ', theQuote)
    print('Fetching Wallet Address: ', address)
    #pause to respect the API if you query the API faster than this you will likely get blacklisted for some time
    print("Waiting 10s to query Blockchain info API... ")
    countdown(10)
    
    if balance is not None:
        print(f'Balance {balance:.8f} BTC')
        print('#############################################################')
        #write quote and balance to results file, if no balance, nothing it written to the file
        #Write each object to the file
        with open(fileOutput, 'a', newline='') as fileOut:
            writer = csv.writer(fileOut)
            writer.writerow([theQuote, address, balance])
        fileOut.close()


# Main
# read in each quote and process it
with open(fileInput, 'r', encoding='UTF-8') as fileIn:
    while line := fileIn.readline():
        line.strip()
        head, sep, tail = line.partition(".")
        testQuote(head)
    fileIn.close()

