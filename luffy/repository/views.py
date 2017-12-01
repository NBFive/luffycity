from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework import serializers
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse

from repository.utils.commons import gen_token
from repository.utils.auth import LuffyAuthentication
# from repository.utils.throttle import LuffyAnonRateThrottle,LuffyUserRateThrottle
# from repository.utils.permission import LuffyPermission
from . import models

from django_redis import get_redis_connection
from luffy import settings
import json


class AuthView(APIView):
    """
    认证相关视图
    """

    def post(self, request, *args, **kwargs):
        """
        用户登录功能
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        ret = {'code': 1000, 'user': '', 'msg': None}
        user = request.data.get('username')
        pwd = request.data.get('password')
        print(request)
        print(request.data)
        print(user, pwd)
        user_obj = models.Account.objects.filter(username=user, password=pwd).first()
        if user_obj:
            tk = gen_token(user)
            models.Token.objects.update_or_create(user=user_obj, defaults={'token': tk})
            ret['code'] = 1001
            ret['user'] = user
            ret['token'] = tk
        else:
            ret['msg'] = "用户名或密码错误"
        response = JsonResponse(ret)
        response['Access-Control-Allow-Origin'] = '*'
        return response


class CourseSerializer(serializers.ModelSerializer):
    """
    序列化
    """
    level = serializers.CharField(source='get_level_display')

    class Meta:
        model = models.Course
        fields = '__all__'


class CourseListView(APIView):
    def get(self, request, *args, **kwargs):
        from django.core.exceptions import ObjectDoesNotExist
        response = {'code': 1000, 'msg': 'ok', 'data': None}
        try:
            course_list = models.Course.objects.exclude(course_type=2)
            ser = CourseSerializer(instance=course_list, many=True, context={'request': request})
            # print(course_list)
            response['data'] = ser.data
        except ObjectDoesNotExist as e:
            response['code'] = 1001
            response['msg'] = '查询课程不存在'
        except IndexError as e:
            pass
        except Exception as e:
            # 错误信息写入日志
            response['code'] = 1001
            response['msg'] = '查询课程失败'

        # response['Access-Control-Allow-Origin'] = '*' # 中间件
        return Response(response)


class CourseDetailSerializer(serializers.ModelSerializer):
    """
    序列化
    """
    course_name = serializers.CharField(source='course.name')
    recommend_courses_list = serializers.SerializerMethodField()
    price_policy_list = serializers.SerializerMethodField()

    class Meta:
        model = models.CourseDetail
        fields = ['id', 'course_name', 'recommend_courses_list', 'price_policy_list']

    def get_recommend_courses_list(self, obj):
        ret = []
        course_list = obj.recommend_courses.all()
        for item in course_list:
            ret.append({'id': item.id, 'name': item.name})
        return ret

    def get_price_policy_list(self, obj):
        ret = []
        price_policy_list = models.PricePolicy.objects.filter(content_type__app_label='repository',
                                                              content_type__model='course',
                                                              object_id=obj.course_id)
        for item in price_policy_list:
            ret.append({'valid_period': item.get_valid_period_display(), 'price': item.price})
        return ret


class CourseDetailView(APIView):
    def get(self, request, *args, **kwargs):

        from django.core.exceptions import ObjectDoesNotExist
        response = {'code': 1000, 'msg': 'ok', 'data': None}
        try:
            pk = kwargs.get('pk')
            course_detail = models.CourseDetail.objects.get(course_id=pk)
            ser = CourseDetailSerializer(instance=course_detail, many=False, context={'request': request})
            # print(course_detail)
            response['data'] = ser.data
        except ObjectDoesNotExist as e:
            response['code'] = 1001
            response['msg'] = '查询课程不存在'
        except IndexError as e:
            pass
        except Exception as e:
            # 错误信息写入日志
            response['code'] = 1001
            response['msg'] = '查询课程失败'

        # response['Access-Control-Allow-Origin'] = '*'  # 中间件
        return Response(response)


class BuyView(APIView):
    def get(self, request):
        self.dispatch()
        conn = get_redis_connection("default")
        accout_id = '1'
        accout_id_en = accout_id.encode('utf-8')
        # d = {accout_id:{
        #     '4': {
        #         'price': 9.9,
        #         'name': '1个月',
        #         'course': {
        #             'id': 2,
        #             'name': 'Python开发21天入门必备',
        #             'img': '2'
        #         }
        #     },
        #     '2': {
        #         'price': 19.9,
        #         'name': '3个月',
        #         'course': {
        #             'id': 1,
        #             'name': '算法入门',
        #             'img': '1'
        #         }
        #     }
        # }}
        # conn.hmset(settings.BUY_INFO_KEY,d)
        # return Response('放入成功')

        # conn.delete(accout_id)
        # return Response(conn.keys())

        buy_dict = conn.hget(settings.BUY_INFO_KEY,accout_id)
        print(buy_dict,type(buy_dict))
        ret = buy_dict.decode('utf-8')
        print(ret,type(ret))
        ret = eval(ret)
        print(ret,type(ret))
        return Response(ret)

        # d = {
        #     accout_id:{
        #         '1':{
        #             'name': '算法入门',
        #             'img': '1',
        #             'selected_policy_id':2,
        #             'policy_list':[
        #                 {'id':1,'name':'1个月','price':9.9},
        #                 {'id':2,'name':'3个月','price':19.9},
        #                 {'id':3,'name':'12个月','price':99.9},
        #             ]
        #         },
        #         '2':{
        #             'name': 'Python开发21天入门必备',
        #             'img': '2',
        #             'selected_policy_id':1,
        #             'policy_list':[
        #                 {'id':4,'name':'1个月','price':9.9},
        #                 {'id':5,'name':'3个月','price':19.9},
        #                 {'id':6,'name':'12个月','price':99.9},
        #             ]
        #         }
        #     }
        # }
        # conn.hmset(settings.CAR_INFO_KEY,d)
        # return Response('放入成功')