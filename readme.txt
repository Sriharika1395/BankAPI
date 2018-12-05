Database name : BankDatabase
Bank Database fields :
{
AccountID:
Password:
CustomerName:
Balance:
}

API:

Login:
FunctionName: Login
Input: AccountNumber, Password
The password entered is compared with the password which is stored in mongodb as an encrypted string.Returns valid if matches else invalid.

GetBalanceInformation:
FunctionName : getBalance
Input : Account ID

AddBeneficiary:
FunctionName : addBeneficiary
Input : AccountID, Customer Name, Balance

DeleteBeneficiary:
FunctionName : deleteBeneficiary
Input : AccountID

TransferFunds:
FunctionName : transferFunds
Input : From Account Number , To Account Number , Amount to be transferred
Checks if the Sender has enough balance, if not notifies else transfers the amount.

Balance in Future:
FunctionName : futureAmount
Input : AccountID , Date for which balance with interest has to be calculated(DD/MM/YYYY)
Calculates the number of days between the current date and given date.Interest is calculated using the formula P*T*R/(100*365) and the balance amount is returned.


