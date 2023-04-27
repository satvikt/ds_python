#
# # def i_am(string):
# #   def one_more_wrapper(func):
# #     def wrapper(*args, **kwargs):
# #       print(string)
# #       func(*args, **kwargs)
# #     return wrapper
# #   return one_more_wrapper
#
# # @i_am("superman")
# # def foo(a, b, c):
# #   print("hello", a, b, c)
#
#
#
# # foo(2,4,5)
#
# # # Output:
# # # --------------
# # # I am superman
# # # hello 2 4 5
# # # --------------
#
#
#
#
# localhost:8000/status
#
# Server A ------ id_a        2sec
# Server B ------ id_b        2sec  
# Server C ------ id_c        2sec
#
# Server X -------- (a,b,c)    -------- res_x    3sec
# Server Y -------- (a,b,c)    -------- res_y    3sec
#
# Response -----> [res_x, res_y]      12 sec
#
#
# GET
# PUT
# POST
# PATCH
# DELETE
#
# def method()
#     # API call
#
#     return Response
#
#
# x -> y -> z
#
# a -> b
#
# x > a > y > z
#
# x > y > z > a > b
#
# docker ps
#
