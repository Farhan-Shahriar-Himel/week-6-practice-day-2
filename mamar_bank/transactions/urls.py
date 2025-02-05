from django.urls import path
from .views import DepositMoneyView, WithdrawMoneyView, TransactionReportView,LoanRequestView,LoanListView,PayLoanView, transfer_money, PasswordChangeClass


# app_name = 'transactions'
urlpatterns = [
    path("deposit/", DepositMoneyView.as_view(), name="deposit_money"),
    path("report/", TransactionReportView.as_view(), name="transaction_report"),
    path("withdraw/", WithdrawMoneyView.as_view(), name="withdraw_money"),
    path("loan_request/", LoanRequestView.as_view(), name="loan_request"),
    path("loans/", LoanListView.as_view(), name="loan_list"),
    path("loans/<int:loan_id>/", PayLoanView.as_view(), name="pay"),
    path("transfer_money/", transfer_money, name='transfer_money'),
    path("change_password/", PasswordChangeClass.as_view(), name='change_password'),
]