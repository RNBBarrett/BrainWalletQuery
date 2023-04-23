
#                      Welcome to BrainWalletQuery


Introduction:
--------------

BrainWalletQuery is a proof of concept used to take in a text quotation from a txt file, convert that to a private key, public key and bitcoin address.

The program then takes the bitcoin address and casually queries the blockchain.info site for an address balance.

This application is made as proof of concept for reading wallet balance ONLY, it is not intended for users to use this material to commit theft. The practice of stealing bitcoin is illegal.

Cybercriminals run automated systems that check the blockchain for known brainwallet addresses, when a balance is added to these accounts these bots automatically work to transfer the balance to the theives address. Use of traditional brainwallets should be avoided. 

For more on this topic see this  [brilliant presentation](https://youtu.be/foil0hzl4Pg) by [Ryan Castelluci](https://github.com/ryancdotorg) at DEF CON 23.

Installation:
--------------

The program is written in python and uses a requirements.txt file to install the dependencies:

At the command line type:

pip install -r requirements.txt


Basic Logic of the Application:
--------------------------------

The application follows this basic logic flow, using this explaination you should be able to walk through the code very easily. It is written in a very simple easy to read format, suitable for the beginner.

Change this string according the name of the txt file your inputting, one quote per line.
fileInput = "quotes.txt" #file you want to read quotes in from, add a director ./mydirectory in front of the filename if your file is in a different folder.

1. Program reads a quote from a fileInput file. Stips off full stops, cleans up the line andpasses the quote into a function def testQuote(theQuote), test quote then immediation passes this quote to bitcoinWalletGenerator().
2. bitcoinWalletGenerator creates a private key, a public key and a bitcoin address and returns the bitcoin address to testQuote.
3. testQuote then takes the wallet address and passes it to check_balance(address).
4. check_balance then makes a request to https://blockchain.info/q/addressbalance/ to see if there is a bitcoin wallet balance associated to the address, it then returns the result back to testQuote.
5. If the balance is not empty check_balance then writes the result to a CSV file. 
6. If a result is not NONE check_balance writes the file to csv. Currently I haven't added any logic not to exclude zero balance, you probably won't find a brain wallet with any balance, so its more exciting to see the logic working and writing out. 

About Brain Wallets:
---------------------

Traditional insecure brainwallets are a type of cryptocurrency wallet that is created by using a simple or easy-to-guess passphrase or seed phrase. These types of brainwallets are considered insecure because the private key can be easily guessed or brute-forced by an attacker, especially if the passphrase or seed phrase is not strong enough.

For example, some people have used common phrases or famous quotations as their brainwallet passphrase, which can be easily guessed by an attacker using automated tools or a dictionary attack. Additionally, some people have used simple sequences of numbers or letters as their seed phrase, which can also be easily guessed or brute-forced.

The problem with traditional insecure brainwallets is that once an attacker is able to guess or obtain the passphrase or seed phrase, they can easily access and spend the funds in the wallet. This can lead to significant financial loss for the owner of the wallet.

In a modern wallet, the seed phrase is typically generated using a cryptographic algorithm that generates a sequence of randomly selected words from a predefined list of words, known as a wordlist. The most commonly used wordlist is the BIP39 wordlist, which consists of 2048 words.

The algorithm uses a cryptographically secure random number generator to generate a series of random numbers, which are then used to select words from the wordlist. The resulting sequence of words is the seed phrase, which is typically 12 to 24 words long.

The advantage of generating a seed phrase in this way is that it is highly random and therefore difficult to guess or brute-force. Additionally, the use of a predefined wordlist ensures that the resulting seed phrase is easy for the user to memorize and enter accurately.

It is important to note that the seed phrase should be kept private and not shared with anyone, as it is the key to access and spend the funds in the wallet.

A bit about Bitcoin Addresses:
-----------------------------

Modern Bitcoin addresses are generated using a process called public key cryptography. Specifically, they are generated using the Elliptic Curve Digital Signature Algorithm (ECDSA), which is a type of public key cryptography that uses elliptic curves to generate public and private key pairs.

To generate a Bitcoin address, the user first generates a private key using a cryptographically secure random number generator. The private key is then used to derive the corresponding public key using the ECDSA algorithm.

The public key is then hashed using the SHA-256 algorithm and the RIPEMD-160 algorithm to produce a unique hash value known as the public key hash. This hash value is then further encoded using the Base58Check encoding scheme to produce the final Bitcoin address.

The resulting Bitcoin address is a string of alphanumeric characters that starts with either "1" or "3", depending on the type of address (i.e., legacy or SegWit).

It is important to note that Bitcoin addresses are derived from the public key hash, not the public key itself. This means that the public key can be kept private, while still allowing the user to receive funds to the Bitcoin address. Additionally, Bitcoin addresses can be generated and used without revealing any personal information about the user.

Future Improvements:
---------------------

This application is a very simple logic exercise and proof of concept, it is not intended to be efficient or have real world use.

Ways to improve on this application would be to perform the following:

1. Gather bitcoin address account balances locally.
2. Store bitcoin addresses with a balance on disk in a bloom filter.
3. Query the brainwallet addresses via bloom filter, threading out each query.

I have not explored it, but it may be possible to download bitcoin addresses with account balances from a source and turn this file into your bloom filter OR it may be possible to install bitcoin core and to query this directly. Other options might include going an API that allows for thousands of queries per second, probably a subscription service.

How does this help security?
-----------------------------

Takeaways are... 

1. Do not use traditional brainwallets, they are insecure.
2. There are a lot of thieves out there with bots who run much more sophisticated systems that will steal your bitcoin account balance in an automated way if you don't protect it properly.
3. Building on simple logic like this might result in a futurue program that could be used by users to watch there account and alert them if there is suspicious activity, maybe an idea of a future app.
