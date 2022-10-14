import json

import requests


def get_headers():
    token = "c30656f4b2c05f7150567ba56dd2ab51aaf0f577cf4277a19d92e9a732289beb"
    request_headers = {"Authorization": "Bearer " + token,
                       "Accept": "application/json", "Content-Type": "application/x-www-form-urlencoded"}
    return request_headers


# 1 create users by reading below data from file (post)
# function i/p file name o/p count of users created
def post_funct(post_file):
    request_url = "https://gorest.co.in/public/v2/users"
    post_list = post_file.readlines()
    post_file.close()
    print("List of users to be created: ", post_list)
    count = len(post_list)
    for user in post_list:
        user_split = user.split()
        name = user_split[0]
        email = user_split[1]
        gender = user_split[2]
        status = user_split[3]
        data1 = {
            "name": name,
            "email": email,
            "gender": gender,
            "status": status
        }
        response = requests.post(url=request_url, data=json.dumps(data1), headers=get_headers())
        print("Post Response code for %s = %s" % (name, response.status_code))
        response_result = response.text
        result = json.loads(response_result)
        # if response.ok:
        #   count = count + 1
        print("Response value = ", result)
    return count


# 2 update below users data status is inactive(patch)
# function i/p file name o/p count of users updated


def patch_funct(patch_file, user_dict):
    patch_users_list = patch_file.readlines()
    patch_file.close()
    print("List of users to be updated: ", patch_users_list)
    count = len(patch_users_list)
    for user in patch_users_list:
        user_split = user.split()
        name = user_split[0]
        email = user_split[1]
        status = "inactive"
        data1 = {
            "name": name,
            "email": email,
            "status": status
        }
        request_url = "https://gorest.co.in/public/v2/users/{id}".format(id=user_dict[name])
        response = requests.patch(url=request_url, data=json.dumps(data1), headers=get_headers())
        print("Patch Response code for %s = %s" % (name, response.status_code))
        # if response.ok:
        #   count = count + 1
        response_result = response.text
        result = json.loads(response_result)
        print("Patch Response value = ", result)
    return count


def get_all_users(file_name):
    users_file = open(file_name, 'w')
    request_url = "https://gorest.co.in/public/v2/users"
    response = requests.get(url=request_url, headers=get_headers())
    print("GET Response code = %s" % response.status_code)
    response_result = response.text
    result = json.loads(response_result)
    dictionary = {}
    for user in result:
        dictionary[user["name"]] = user["id"]
    users_file.write(str(result))
    return dictionary


def delete_funct(delete_file, user_dict):
    delete_users_list = delete_file.readlines()
    delete_file.close()
    print("List of users to be deleted: ", delete_users_list)
    count = len(delete_users_list)
    for user in delete_users_list:
        user_split = user.split()
        name = user_split[0]
        request_url = "https://gorest.co.in/public/v2/users/{id}".format(id=user_dict[name])
        response = requests.patch(url=request_url, headers=get_headers())
        print("Delete Response code for %s = %s" % (name, response.status_code))
        # if response.ok:
        #   count = count + 1
        response_result = response.text
        result = json.loads(response_result)
        print("Delete Response value = ", result)
    return count
