
#  DamnPhish

Phishing is a type of cyber threat practice where, the intruder acts as a trustworthy entity and
attempts to steal sensitive information such as Login Credentials, Credit and Debit card details
by making the user feel the websites look and feel exactly as the original ones. It is generally
carried out in various ways like E-Mail Spoofing, Instant Messaging or redirecting to the fake
websites which user cannot detect the differences between the original and malicious ones.

The  core  idea  of  this  project  is  to  detect  those  phishing  websites  by  analysing  the
characteristics of URL (Uniform Resource Locator) using Machine Learning Algorithms.
We analyse various features of the URL like presence of ‘@’ symbol, presence of Redirection
(//) Symbol, Length of URL, Subdomains present in the URL which are relevant to the system
and help in performing prediction on a new URL. All these extracted features are then trained
in to a best suited machine learning algorithm. These features play a major role in classifying
a URL whether a safe one or malicious.

The data we have used here is in high-level language which is first converted into machine-
level language first and then these features are used as parameters to train the model. We have
designed a web-app where the user can upload a file of URLs that he/she wants to predict and
then obtain a result from it. With the assistance of this project, one can easily stop entering
malicious websites and be safe from potential cyber threats
