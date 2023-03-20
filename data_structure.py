'''list = []

print(type(list))

list.append(1)
list.append(2)
list.append(3)
list.append("Sumit")
list.pop()
list.reverse()
print(list)'''

cloud_list = ["AWS", "GCP", "Azure", "Oracle", "IBM"]
env_list = ["dev", "Prod", "test"]

print(cloud_list[0])

print(env_list[2])

#for s in range(10):
 #   print(s)

#List Iteration ->
for cloud in cloud_list:
    if cloud == "AWS":
        print("I know AWS platform only")


#Dictionary
dict_of_cloud = {
    "AWS":"Amazon Web Services", "Azure":"Microsoft Azure", "GCP":"Google Cloud Platform"
}

#getting the info
print(dict_of_cloud["AWS"])
print(dict_of_cloud.get("GCP"))

# Update - adding new object in existing dictionary
dict_of_cloud.update({"alibaba":"Cloud Service Provider"})

print(dict_of_cloud)

print(dict_of_cloud["alibaba"])

