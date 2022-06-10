from rest_framework.throttling import UserRateThrottle

class ReviewCreateThrottle(UserRateThrottle):
    """Define Scope"""
    scope = "review_create"
    
class ReviewListThrottle(UserRateThrottle):
    """Define Scope"""
    scope = "review_list"
