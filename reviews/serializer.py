from rest_framework import serializers
from reviews.models import Reviews




class ReviewsSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only= True)
    user_id = serializers.StringRelatedField(read_only= True)
    rate = serializers.FloatField(read_only= True)
    review = serializers.CharField(read_only= True)
    review_date = serializers.DateField(read_only= True)


    def create(self, validate_data):
        return Reviews.objects.create(**validate_data)


    class Meta:
        model = Reviews
        fields = '__all__'