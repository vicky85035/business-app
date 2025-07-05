import pytz
import uuid
from django.db import models
from libs.model_mixin import BaseModelMixin

class Category(models.Model):
	name = models.CharField(max_length=50)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = "Categories"

class Marketing(BaseModelMixin):
	"""model for define the business type or industry
	belongs to the business"""

	name = models.CharField(max_length=200, null=True, blank=True)
	user = models.OneToOneField(
		"accounts.User", on_delete=models.CASCADE, related_name="marketing")

	class Meta:
		verbose_name = "Marketing"
		verbose_name_plural = "Marketings"
		app_label = "business"

	def __str__(self):
		return self.name


class Business(BaseModelMixin):
	"""model for established business"""
	name = models.CharField(max_length=200, null=True, blank=True)
	logo = models.ImageField(null=True, blank=True)
	user = models.ForeignKey(
		"accounts.User",
		on_delete=models.CASCADE,
		related_name="business_as_owner")
	marketing = models.ForeignKey(
		"business.Marketing",
		related_name="business",
		on_delete=models.CASCADE, null=True, blank=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
	business_manager = models.ForeignKey(
		"accounts.User", related_name="business_manager", on_delete=models.CASCADE, null=True, blank=True)
	smart_response = models.BooleanField(default=True)
	ai_response = models.BooleanField(default=False)
	enable_ticket_resolution = models.BooleanField(default=False)
	enable_product_issue_reasons_mapping_questions = models.BooleanField(default=False)
	disable_comment_section_in_ticket_review_modal = models.BooleanField(default=False)
	restrict_ticket_closing_without_submitting_ticket_survey = models.BooleanField(default=False)
	reviews_fetching = models.BooleanField(default=False)
	account_suspended = models.BooleanField(default=False)
	team = models.ManyToManyField("accounts.User")
	# api_key = models.CharField(max_length=200, null=True, blank=True)
	business_uuid = models.UUIDField(null=True, blank=True, default=uuid.uuid4)
	is_sms_allowed = models.BooleanField(default=False)
	send_sms_to_customer_for_qr_reviews = models.BooleanField(default=False)
	is_whatsapp_allowed = models.BooleanField(default=False)

	class Meta:
		verbose_name = "Business"
		verbose_name_plural = "Businesses"


	def __str__(self):
		return self.name



class Branch(BaseModelMixin):
	"""Branch model of a business """

	LANGUAGES = (('english', 'English'), ('hindi', 'Hindi'))
	TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))

	name = models.CharField(verbose_name='Branch name:',max_length=250, null=True, blank=True)
	branch_owner = models.ManyToManyField("accounts.User", related_name="branches")

	business = models.ForeignKey(Business, related_name="branches", on_delete=models.CASCADE)
	category = models.ForeignKey(Category, related_name='branches', on_delete=models.CASCADE, null=True, blank=True,)
	address = models.ForeignKey(
		"business.Address", related_name="addresses",
		on_delete=models.CASCADE, null=True, blank=True
	)
	created_at = models.DateField(auto_now_add=True, null=True, blank=True)
	branch_city = models.CharField(max_length=250, null=True, blank=True)
	branch_state = models.CharField(max_length=250, null=True, blank=True)
	location_address = models.CharField(max_length=300)
	pincode = models.IntegerField(default=0)
	alias = models.CharField(max_length=250, null=True, blank=True)
	contact_number = models.CharField(null=True, blank=True)
	working_hours = models.CharField(max_length=250, null=True, blank=True)
	is_corporate = models.BooleanField(default=False)
	website = models.URLField(help_text='website of the branch/business', null=True, blank=True)
	description = models.TextField(null=True, blank=True)
	languages = models.CharField(
		max_length=20, choices=LANGUAGES, null=True, blank=True)
	timezone = models.CharField(
		max_length=32, choices=TIMEZONES, default='UTC')
	added_by = models.ForeignKey("accounts.User", on_delete=models.CASCADE, null=True, blank=True,
								 related_name="added_branch")
	email = models.EmailField(null=True, blank=True)
	fb_page_id = models.CharField(max_length=250, null=True, blank=True)

	class Meta:
		verbose_name = "Branch"
		verbose_name_plural = "Branches"
		app_label = "business"

	def __str__(self):
		return f'{self.business} from {self.name}'


class Address(BaseModelMixin):
	formatted_address = models.CharField(max_length=300)
	city = models.CharField(max_length=100, null=True, blank=True)
	state = models.CharField(max_length=100, null=True, blank=True)
	country = models.CharField(max_length=100, null=True, blank=True)
	postal_code = models.CharField(max_length=12, null=True, blank=True)
	business_status = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.formatted_address

	class Meta:
		verbose_name_plural = "Addresses"


class WebPortal(BaseModelMixin):
	""" model for web provider """
	API = 'api'
	SCRAPPER = 'scrapper'
	SOURCE_CHOICE = (
		(API, "api"),
		(SCRAPPER, "scrapper")
	)

	REVIEW = 'Review'
	MENTION = 'Mention'
	COMPLAINT = 'Complaint'
	MESSAGES = "Messages"
	PROVIDER_TYPE_CHOICE = (
		(REVIEW, "Review"),
		(MENTION, "Mention"),
		(COMPLAINT, "Complaint"),
		(MESSAGES, "Messages")
	)

	provider = models.CharField(
		max_length=50, help_text="Rating provider sites name")

	is_auth_required = models.BooleanField(default=False, db_index=True)
	is_link_required = models.BooleanField(default=True, db_index=True)
	is_reply_allow = models.BooleanField(default=True)
	source_type = models.CharField(choices=SOURCE_CHOICE, null=True, blank=True)
	provider_type = models.CharField(choices=PROVIDER_TYPE_CHOICE, null=True, blank=True)
	priority = models.SmallIntegerField(null=True, blank=True)
	provider_uuid = models.UUIDField(null=True, blank=True, default=uuid.uuid4)
	provider_logo = models.ImageField(upload_to='logo_image', null=True, blank=True)

	class Meta:
		verbose_name = "Web Portal"
		verbose_name_plural = "Web Portals"
		app_label = "business"

	def __str__(self):
		return self.provider
