from django.conf.urls import patterns,include,url
urlpatterns=patterns('',
	url(r'^BillPaymentForm/$','maintainbill.views.renderBillPayment',name='BillPaymentForm'),
	url(r'^BillPayment/$','maintainbill.views.handleBillPayment',name='BillPayment'),
	#url(r'^confirm/$','maintainbill.views.handleConfirm',name='handleConfirm'),
	#url(r'^rconfirm/$','maintainbill.views.renderConfirm',name='renderConfirm'),
	url(r'^BillAddForm/$','maintainbill.views.renderBillAdd',name='BillAddForm'),
	url(r'^BillAdd/$','maintainbill.views.handleBillAdd',name='BillAdd'),
	url(r'^(?P<id>\d+)/BillUpdateForm/$','maintainbill.views.renderBillUpdate',name='BillUpdateForm'),
	url(r'^(?P<id>\d+)/BillUpdate/$','maintainbill.views.handleBillUpdate',name='BillUpdate'),
	url(r'^BillDeleteForm/$','maintainbill.views.renderBillDelete',name='BillDeleteForm'),
	url(r'^BillDelete/$','maintainbill.views.handleBillDelete',name='BillDelete'),
	url(r'^BillViewForm/$','maintainbill.views.renderBillView',name='BillViewForm'),
	url(r'^BillView/$','maintainbill.views.handleBillView',name='BillView'),
	url(r'^Bills/$','maintainbill.views.Bills',name='Bills'),
	url(r'^rloginservice/$','maintainbill.views.renderLoginService', name='rloginservice'),
	url(r'^rsignupservice/$','maintainbill.views.renderSignupService', name='rsignupservice'),
	url(r'^loginservice/$','maintainbill.views.handleLoginService', name='loginservice'),
	url(r'^signupservice/$','maintainbill.views.handleSignupService', name='signupservice'),
	url(r'^mainservice/$','maintainbill.views.mainservice', name='mainservice'),
	url(r'^logoutservice/$','maintainbill.views.logoutservice', name='logoutservice'),
)
