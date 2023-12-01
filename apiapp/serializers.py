from rest_framework import serializers

class Generate_Info_Title_Serializer(serializers.Serializer):
    input_text = serializers.CharField(max_length=1000)



class Generate_Info_Outline_Serializer(serializers.Serializer):
    input_text = serializers.CharField(max_length=3000)