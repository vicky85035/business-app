from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)
from django.db import models
from libs.model_mixin import BaseModelMixin


class UserManager(BaseUserManager):

    def _create_user(self, email, password,is_staff, is_superuser, **extra_fields):
        """

        Creates and saves a User with the given email and password.

        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        if is_superuser:
            extra_fields['is_active'] = is_superuser
            extra_fields['business_type'] = self.model.MARKETING
        user = self.model(email=email,
                          is_staff=is_staff,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, False, False,**extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True,**extra_fields)
    



class User(AbstractBaseUser, PermissionsMixin, BaseModelMixin):

    BUSINESS    = "business"
    ENTERPRISES = "enterprises"
    MARKETING   = "marketing"

    BUSINESS_TYPE = (
        (BUSINESS, "Single Location Business"),
        (ENTERPRISES, "Multiple Location Business"),
        (MARKETING, "Marketing Agency"),
    )

    ONE_RATING   = "1"
    TWO_RATING   = "2"
    THREE_RATING = "3"
    FOUR_RATING  = "4"
    FIVE_RATING  = "5"

    RATING_OPTIONS = (
        (ONE_RATING, "ONE_RATING"),
        (TWO_RATING, "TWO_RATING"),
        (THREE_RATING, "THREE_RATING"),
        (FOUR_RATING, "FOUR_RATING"),
        (FIVE_RATING, "FIVE_RATING"),
    )

    DAY     = "DAY"
    WEEKLY  = "WEEKLY"
    MONTHLY = "MONTHLY"

    ALERTS = (
        (DAY, "Daily"),
        (WEEKLY, "Weekly"),
        (MONTHLY, "Monthly")
    )
    
    WHATSAPP_ALERTS_NEGATIVE_REVIEWS_All_CONTENT = '1'
    WHATSAPP_ALERTS_NEGATIVE_REVIEWS_ONLY_WITH_CONTENT = '2'
    WHATSAPP_ALERTS_NEUTRAL_REVIEWS_All_CONTENT = '3'
    WHATSAPP_ALERTS_NEUTRAL_REVIEWS_ONLY_WITH_CONTENT = '4'
    WHATSAPP_ALERTS_COMPLAINTS_ALL_CONTENT = '5'

    WHATSAPP_ALERTS = (
        (WHATSAPP_ALERTS_NEGATIVE_REVIEWS_All_CONTENT, "Whatsapp_Alerts_Negative_Reviews_All_Content"),
        (WHATSAPP_ALERTS_NEGATIVE_REVIEWS_ONLY_WITH_CONTENT, "Whatsapp_Alerts_Negative_Reviews_Only_With_Content"),
        (WHATSAPP_ALERTS_NEUTRAL_REVIEWS_All_CONTENT, "Whatsapp_Alerts_Neutral_Reviews_All_Content"),
        (WHATSAPP_ALERTS_NEUTRAL_REVIEWS_ONLY_WITH_CONTENT, "Whatsapp_Alerts_Neutral_Reviews_Only_With_Content"),
        (WHATSAPP_ALERTS_COMPLAINTS_ALL_CONTENT, "Whatsapp_Alerts_Complaints_All_Content"),
    )

    first_name      = models.CharField('First Name', max_length=30, db_index=True)
    last_name       = models.CharField('Last Name', max_length=30, db_index=True)
    email           = models.EmailField('Email address', max_length=254, unique=True, db_index=True)
    avatar           = models.ImageField(upload_to="profile/", null=True, blank=True)
    contact_number  = models.CharField(max_length=30, null=True, blank=True)
    business_type   = models.CharField(choices=BUSINESS_TYPE, max_length=200, default=BUSINESS)
    is_active       = models.BooleanField(default=False)
    approved        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    date_joined     = models.DateTimeField(auto_now=True)
    is_superuser    = models.BooleanField(default=False)
    email_alert     = models.BooleanField(default=False)
    sms_alert       = models.BooleanField(default=False)

    daily_dining_display_report                                 = models.BooleanField(default=True,verbose_name='Display Rating Report')
    daily_city_brand_channel_wise_average_rating_email_alert    = models.BooleanField(default=False)
    weekly_city_brand_channel_wise_average_rating_email_alert   = models.BooleanField(default=False)
    monthly_city_brand_channel_wise_average_rating_email_alert  = models.BooleanField(default=False)
    daily_city_brand_channel_wise_no_of_rating_email_alert      = models.BooleanField(default=False)
    weekly_city_brand_channel_wise_no_of_rating_email_alert     = models.BooleanField(default=False)
    monthly_city_brand_channel_wise_no_of_rating_email_alert    = models.BooleanField(default=False)

    daily_summary_rating_email_alert                        = models.BooleanField(default=False)
    weekly_summary_rating_email_alert                       = models.BooleanField(default=False)
    monthly_summary_rating_email_alert                      = models.BooleanField(default=False)
    daily_outlet_wise_channel_wise_ratings_email_alert      = models.BooleanField(default=False)
    weekly_outlet_wise_channel_wise_ratings_email_alert     = models.BooleanField(default=False)
    monthly_outlet_wise_channel_wise_ratings_email_alert    = models.BooleanField(default=False)
    daily_critical_review_email_alert                       = models.BooleanField(default=False)
    weekly_critical_review_email_alert                      = models.BooleanField(default=False)
    monthly_critical_review_email_alert                     = models.BooleanField(default=False)
    daily_detailed_review_email_alert                       = models.BooleanField(default=False)
    weekly_detailed_review_email_alert                      = models.BooleanField(default=False)
    monthly_detailed_review_email_alert                     = models.BooleanField(default=False)
    daily_overall_issue_email_alert                         = models.BooleanField(default=False)
    weekly_overall_issue_email_alert                        = models.BooleanField(default=False)
    monthly_overall_issue_email_alert                       = models.BooleanField(default=False)
    daily_summary_issue_email_alert                         = models.BooleanField(default=False)
    weekly_summary_issue_email_alert                        = models.BooleanField(default=False)
    monthly_summary_issue_email_alert                       = models.BooleanField(default=False)
    daily_consolidated_email_alert                          = models.BooleanField(default=False)
    weekly_consolidated_email_alert                         = models.BooleanField(default=False)
    monthly_consolidated_email_alert                        = models.BooleanField(default=False)

    daily_brand_wise_rating_summary_email_alert             = models.BooleanField(default=False)
    weekly_brand_wise_rating_summary_email_alert            = models.BooleanField(default=False)
    monthly_brand_wise_rating_summary_email_alert           = models.BooleanField(default=False)

    daily_brand_wise_tag_summary_email_alert             = models.BooleanField(default=False)
    weekly_brand_wise_tag_summary_email_alert            = models.BooleanField(default=False)
    monthly_brand_wise_tag_summary_email_alert           = models.BooleanField(default=False)

    daily_offline_qr_code_report                            = models.BooleanField(default=False)
    weekly_offline_qr_code_report                           = models.BooleanField(default=False)
    monthly_offline_qr_code_report                          = models.BooleanField(default=False)

    daily_star_rating_email_alert                           = models.BooleanField(default=False)
    weekly_star_rating_email_alert                          = models.BooleanField(default=False)
    monthly_star_rating_email_alert                         = models.BooleanField(default=False)

    weekly_digest                                           = models.BooleanField(default=False,help_text="Weekly Outlet wise Email Alert - NPS, Sources Status, Response Status, Ticket Status, Top Negative and Positive Reviews")
    daily_digest                                            = models.BooleanField(default=False,help_text="Daily Outlet wise Email Alert - NPS, Sources Status, Response Status, Ticket Status," "Top Negative and Positive Reviews")
    ratings_alert                                           = models.CharField(choices=RATING_OPTIONS, null=True, blank=True)
    alerts_schedule                                         = models.CharField(choices=ALERTS, null=True, blank=True)
    manager                                                 = models.ForeignKey("accounts.User",related_name="teams", on_delete=models.CASCADE, null=True, blank=True)

    enable_review_reply                                     = models.BooleanField(default=False)
    enable_ticket_creation                                  = models.BooleanField(default=False)
    enable_offline_forms                                    = models.BooleanField(default=False)
    enable_customer_care_forms                              = models.BooleanField(default=False)
    enable_swiggy_forms                                     = models.BooleanField(default=False)
    enable_zomato_forms                                     = models.BooleanField(default=False)
    enable_magic_pin_forms                                  = models.BooleanField(default=False)
    enable_ticket_activity                                  = models.BooleanField(default=False)
    enable_ticket_assign                                    = models.BooleanField(default=False)
    enable_ticket_close                                     = models.BooleanField(default=False)
    send_emergency_mail                                     = models.BooleanField(default=True)
    send_qr_report_mail                                     = models.BooleanField(default=False)
    enable_mention_action                                   = models.BooleanField(default=False)
    daily_complaint_report_email_alert                      = models.BooleanField(default=False)
    weekly_complaint_report_email_alert                     = models.BooleanField(default=False)
    monthly_complaint_report_email_alert                    = models.BooleanField(default=False)

    send_complaint_email                                    = models.BooleanField(default=False)
    whatsapp_alert                                          = models.BooleanField(default=False)
    zomato_complaint_button                                 = models.BooleanField(default=False)
    swiggy_complaint_button                                  = models.BooleanField(default=False)
    whatsapp_alert_options                                  = models.CharField(choices=WHATSAPP_ALERTS, null=True, blank=True)
    enable_sr_module                                        = models.BooleanField(null=True, blank=True)
    out_stock_email_alert                                   = models.BooleanField(default=True,null=True, blank=True)
    offline_store_email_alert                               = models.BooleanField(default=True,null=True, blank=True)
    last_otp                                                = models.CharField(max_length=10, blank=True, null=True)
    has_two_factor_auth                                     = models.BooleanField(default=False, null=True, blank=True)
    enable_contact_page                                     = models.BooleanField(default=False, null=True, blank=True)
    enable_listing_product                                  = models.BooleanField(default=False, null=True, blank=True)
    enable_marketplace                                      = models.BooleanField(default=False, null=True, blank=True)
    enable_whatsapp                                         = models.BooleanField(default=False, null=True, blank=True)
    enable_review                                           = models.BooleanField(default=True, null=True, blank=True)
    enable_social                                           = models.BooleanField(default=False, null=True, blank=True)
    enable_complaint_refund                                 = models.BooleanField(default=False, null=True)

    objects = UserManager()

    USERNAME_FIELD  = "email"
    REQUIRED_FIELDS = ['first_name']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.email

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return '%s %s' % (self.first_name, self.last_name)

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def is_single_business(self):
        """ check user is single  business """
        return self.business_type == self.BUSINESS

    def is_marketing_agency(self):
        """ check user is marketing agency """
        return self.business_type == self.MARKETING

    def is_enterpriser(self):
        """ check user is enterprises """
        return self.business_type == self.ENTERPRISES

    def is_user_profile_complete(self):
        """check whether the profile is completed or not"""
        if self.business_type:
            return True
        else:
            return False

    def is_business_profile_complete(self):
        """ check user has set their business or not """
        if self.is_marketing_agency():
            return True
        elif self.branches.exists():
            return True
        else:
            return False

    def is_marketing_business_user(self):
        try:
            business = get_object_or_404(Business, id=self.business)
            if business.marketing and business.user == self and not \
                    self.get_marketing():
                return True
            else:
                return False
        except Exception:
            return False

    def marketing_business_screen_name(self):
        screen_name = []
        if not self.is_user_profile_complete():
            screen_name.append("PROFILE")
        if not get_object_or_404(Business, id=self.business).branches.exists():
            screen_name.append("BUSINESS_BRANCH")
        return screen_name

    @property
    def screen_name(self):
        screen_name = []
        if self.is_marketing_business_user():
            screen = self.marketing_business_screen_name()
            screen_name.append(screen)
            return screen_name
        if not self.is_user_profile_complete():
            screen_name.append("PROFILE")
        if not self.is_business_profile_complete():
            screen_name.append("BUSINESS_BRANCH")
        return screen_name

    @property
    def name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        return str(self.first_name) + ' ' + str(self.last_name)

    @property
    def business(self):
        try:
            branch = self.branches.first()
            if self.business_as_owner.exists():
                return self.business_as_owner.first().id
            elif branch:
                return branch.business.id
            elif self.get_marketing():
                return self.get_marketing().business.first().id
            else:
                return Business.objects.filter(team__in=[self,]).first().id
        except Exception:
            return None
    
    @property
    def allowed_businesses(self):
        try:
            if self.get_marketing():
                return list(self.get_marketing().business.all().values_list('id', flat=True))
            
            if Branch.objects.filter(branch_owner = self).count() > 1:
                return list(Branch.objects.filter(branch_owner = self).values_list('business_id', flat=True).distinct())
            
            if self.business_as_owner.exists():
                return [self.business_as_owner.first().id]
           
            branch = self.branches.first()
            if branch:
                return [branch.business.id]
            return [Business.objects.filter(team__in=[self,]).first().id]
        except:
            return []
        
    @property
    def business_list(self):
        try:
            if self.business_as_owner.exists():
                return [self.business_as_owner.first().id]
            else:
                business_ids = Business.objects.filter(team__in=[self,]).values_list('id', flat=True)
                return business_ids
        except Exception:
            return []

    @property
    def business_name(self):
        branch = self.branches.first()
        if branch:
            return branch.business.name
        elif self.business_as_owner.exists():
            return self.business_as_owner.first().name
        else:
            return None

    @property
    def corporate_branch(self):
        """ get the user corporate branch id """
        if Business.objects.filter(user=self).exists():
            branch = get_object_or_404(Business, id=self.business).branches.first()
        else:
            branch = self.branches.first()
        if branch:
            return branch.id
        else:
            return None


    def get_team_members(self):
        """ get the team members of all """
        if self.manager:
            return self.manager.teams.all()
        else:
            return self.teams.all()

    def get_marketing(self):
        if hasattr(self, "marketing"):
            return self.marketing
        else:
            return None

    def is_manager(self, user):
        return self == user.manager

    def save(self, *args, **kwargs):
        if self.pk is None:
            self.email_alert     = True
            self.sms_alert       = False
            self.ratings_alert   = [User.ONE_RATING, User.TWO_RATING,User.THREE_RATING, User.FOUR_RATING,User.FIVE_RATING]
            self.alerts_schedule = [User.DAY]
        super(User, self).save(*args, **kwargs)

    def block_user(self):
        self.is_active = False


class ContactList(BaseModelMixin):

    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

    GENDER = (
        (MALE, "Male"),
        (FEMALE, "Female"),
        (OTHER, "Other")
    )

    branch = models.ForeignKey(
        "business.Branch", on_delete=models.CASCADE,
        db_index=True
    )
    name                    = models.CharField(max_length=254, db_index=True)
    email                   = models.EmailField(max_length=254, null=True, blank=True, db_index=True)
    contact_number          = models.CharField(null=True, blank=True, db_index=True)
    gender                  = models.CharField(max_length=10, choices=GENDER, default=OTHER)
    city                    = models.CharField(max_length=150, null=True, blank=True)
    restrict_communication  = models.BooleanField(default=False)
    unique_code             = models.CharField(max_length=256, null=True, blank=True)
    dob                     = models.DateField(null=True, blank=True)
    anniversary             = models.DateField(null=True, blank=True)
    visites                 = models.IntegerField(default=0)
    last_visit              = models.DateTimeField(null=True, blank=True)
    
    
    def __str__(self):
        return self.name


class AgencyStaff(models.Model):
    marketing = models.ForeignKey("business.Marketing", related_name="agency_staff_marketing", on_delete=models.CASCADE)
    business = models.ForeignKey("business.Business", related_name="agency_staff_business", on_delete=models.CASCADE)
    branch    = models.ManyToManyField("business.Branch", related_name="agency_branch")
    staff = models.ManyToManyField("accounts.User",related_name="agency_staff")
    new_assigned = models.ManyToManyField("accounts.User",related_name="new_assigned")
    name = models.CharField(max_length=256, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Agency Staff"
        verbose_name_plural = "Agency Staff"

    def __str__(self):
        return  str(self.marketing) + "-- agency --" + str(self.business)
