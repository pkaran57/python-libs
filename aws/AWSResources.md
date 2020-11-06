# AWS Resources

## Python SDK

[SDK](https://aws.amazon.com/sdk-for-python/)  
[SDK Doc](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)  
[Available Services](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/index.html)  

High Level Concepts:
* [Low-level clients](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html)  
Clients provide a low-level interface to AWS whose methods map close to 1:1 with service APIs. All service
 operations are supported by clients. Clients are generated from a JSON service definition file.

* [Resources](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html#resources)  
Resources represent an object-oriented interface to Amazon Web Services (AWS). They provide a higher-level abstraction than the raw, low-level calls made by service clients.

* [Collections](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/collections.html)  
A collection provides an iterable interface to a group of resources. A collection seamlessly handles pagination for you, making it possible to easily iterate over all items from all pages of data.

* [Paginators](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/paginators.html)  
Some AWS operations return results that are incomplete and require subsequent requests in order to attain the entire result set. The process of sending subsequent requests to continue where a previous request left off is called pagination. 
Paginators are a feature of boto3 that act as an abstraction over the process of iterating over an entire result set
 of a truncated API operation.
 
* Waiters  
Boto3 comes with 'waiters', which automatically poll for pre-defined status changes in AWS resources. For example, you can start an Amazon EC2 instance and use a waiter to wait until it reaches the 'running' state, or you can create a new Amazon DynamoDB table and wait until it is available to use. Boto3 has waiters for both client and resource APIs.
