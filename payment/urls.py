from django.conf.urls import include,patterns,url
urlpatterns=patterns('',
    url(r'^Payment/$','payment.views.ShowEnterId',name='ShowEnterId'),
    url(r'^CheckBill/$','payment.views.ShowPayment', name='ShowPayment'),
    url(r'^rotp/$','payment.views.renderOtp',name='rotp'),
    url(r'^ConfirmPayment/$','payment.views.MakePayment', name='MakePayment'),
)
