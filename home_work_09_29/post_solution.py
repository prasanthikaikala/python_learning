# 1 create users by reading below data from file (post)
# function i/p file name o/p count of users create

from post_function import post_funct, get_all_users, patch_funct, delete_funct

post_file_path = 'C:\\Users\\kaika\\Desktop\\prasanthi\\home_work_09_29\\post_file.txt'
post_file = open(post_file_path, 'r')

count = post_funct(post_file)
print("Created %s, new users" % count)

get_output_file_path = 'C:\\Users\\kaika\\Desktop\\prasanthi\\home_work_09_29\\users_file.txt'
users_dict = get_all_users(get_output_file_path)
print("Users : ", users_dict)

patch_file_path = 'C:\\Users\\kaika\\Desktop\\prasanthi\\home_work_09_29\\patch_file.txt'
patch_file = open(patch_file_path, 'r')
print("Updated %s users" % patch_funct(patch_file, users_dict))

delete_file_path = 'C:\\Users\\kaika\\Desktop\\prasanthi\\home_work_09_29\\delete_file.txt'
patch_file = open(delete_file_path, 'r')
print("Deleted %s users" % delete_funct(patch_file, users_dict))