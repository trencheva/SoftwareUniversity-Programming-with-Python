from project.campaigns.base_campaign import BaseCampaign
from project.influencers.base_influencer import BaseInfluencer


class StandardInfluencer(BaseInfluencer):
    INITIAL_PAYMENT_PERCENTAGE = 45

    def calculate_payment(self, campaign: BaseCampaign):
        return float(campaign.budget * (self.INITIAL_PAYMENT_PERCENTAGE / 100))

    def reached_followers(self, campaign_type: str):

        if campaign_type == 'HighBudgetCampaign':
            return int((self.followers * self.engagement_rate) * 1.2)
        elif campaign_type == 'LowBudgetCampaign':
            return int((self.followers * self.engagement_rate) * 0.9)
