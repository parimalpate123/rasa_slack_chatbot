## greet
* greet
    - utter_greet

## thank
* thank
    - utter_thank

## bye
* bye
    - utter_bye










## trigger_jenkinsjob
* trigger_jenkinsjob
	- action_jenkins
	- slot{"requested_slot": "jenkinsjob"}
* inform{"jenkinsjob": "sampleapp_ppl"}
	- action_jenkins
	- slot{"jenkinsjob": "sampleapp_ppl"}
	
## trigger_jenkinsjob
* greet
    - utter_greet
* trigger_jenkinsjob
	- action_jenkins
	- slot{"requested_slot": "jenkinsjob"}
* inform{"jenkinsjob": "sampleapp_ppl"}
	- action_jenkins
	- slot{"jenkinsjob": "sampleapp_ppl"}
	
## trigger_jenkinsjob
* greet
    - utter_greet
* trigger_jenkinsjob
	- action_jenkins
	- slot{"requested_slot": "jenkinsjob"}
* inform{"jenkinsjob": "sampleapp_ppl"}
	- action_jenkins
	- slot{"jenkinsjob": "sampleapp_ppl"}
* thank
    - utter_thank
* bye
    - utter_bye










## trigger_deploy
* trigger_deploy
	- action_jenkins_param
	- slot{"requested_slot": "appname"}
* inform{"appname": "deploytest"}
	- action_jenkins_param
	- slot{"appname": "deploytest"}
	- slot{"requested_slot": "environment"}
* inform{"environment": "uat"}
	- action_jenkins_param
	- slot{"environment": "uat"}
	
## trigger_deploy
* trigger_deploy
	- action_jenkins_param
	- slot{"requested_slot": "appname"}
* inform{"appname": "deploytest"}
	- action_jenkins_param
	- slot{"appname": "deploytest"}
	- slot{"requested_slot": "environment"}
* inform{"environment": "int"}
	- action_jenkins_param
	- slot{"environment": "int"}

## trigger_deploy
* greet
    - utter_greet
* trigger_deploy
	- action_jenkins_param
	- slot{"requested_slot": "appname"}
* inform{"appname": "deploytest"}
	- action_jenkins_param
	- slot{"appname": "deploytest"}
	- slot{"requested_slot": "environment"}
* inform{"environment": "int"}
	- action_jenkins_param	
	- slot{"environment": "int"}
	
## trigger_deploy
* greet
    - utter_greet
* trigger_deploy
	- action_jenkins_param
	- slot{"requested_slot": "appname"}
* inform{"appname": "deploytest"}
	- action_jenkins_param
	- slot{"appname": "deploytest"}
	- slot{"requested_slot": "environment"}
* inform{"environment": "prod"}
	- action_jenkins_param	
	- slot{"environment": "prod"}

## trigger deploy
* trigger_deploy{"appname": "deploytest","environment": "uat"}
	- action_jenkins_param

## trigger deploy
* trigger_deploy{"appname": "deploytest","environment": "prod"}
	- action_jenkins_param
	






	



## check_status_withID1
* check_JIRA_Status
    - action_GetJIRAStatus_param
	- slot{"requested_slot": "JIRAID"}
* inform{"JIRAID": "TS-3"}
	- action_GetJIRAStatus_param
	- slot{"JIRAID": "TS-3"}
	
	
## check_jira_request1
* greet
    - utter_greet
* check_JIRA_Status
    - action_GetJIRAStatus_param
	- slot{"requested_slot": "JIRAID"}
* inform{"JIRAID": "TS-3"}
	- action_GetJIRAStatus_param
	- slot{"JIRAID": "TS-3"}
	
## create JIRA ISSUE
* greet
    - utter_greet
* create_JIRA_request
	- action_createJIRArequest_param
	- slot{"requested_slot": "description"}
* inform{"description": "test"}
	- action_createJIRArequest_param
	- slot{"description": "test"}
	- slot{"requested_slot": "summary"}
* inform{"summary": "summary"}
	- action_createJIRArequest_param
	- slot{"summary": "summary"} 
	
## create JIRA ISSUE
* create_JIRA_request
	- action_createJIRArequest_param
	- slot{"requested_slot": "description"}
* inform{"description": "test"}
	- action_createJIRArequest_param
	- slot{"description": "test"}
	- slot{"requested_slot": "summary"}
* inform{"summary": "summary"}
	- action_createJIRArequest_param
	- slot{"summary": "summary"}


## create JIRA REQUEST
* create_JIRA_request
	- action_createJIRArequest_param
	- slot{"requested_slot": "description"}
* inform{"description": "test"}
	- action_createJIRArequest_param
	- slot{"description": "test"}
	- slot{"requested_slot": "summary"}
* inform{"summary": "summary example"}
	- action_createJIRArequest_param
	- slot{"summary": "summary example"}

## create JIRA request
* create_JIRA_request{"description": "test","summary": "summary example"}
	- action_createJIRArequest_param
	
## create JIRA Request
* create_JIRA_request{"description": "test","summary": "access required"}
	- action_createJIRArequest_param
	
## create JIRA Request
* create_JIRA_request{"description": "test","summary": "summary"}
	- action_createJIRArequest_param













		
## CHECK SERVICE
*check_service
	- action_checkservice
	- slot{"requested_slot": "servicename"}
* inform{"servicename": "google"}
	- action_checkservice
	- slot{"servicename": "google"}

## CHECK SERVICE
*check_service
	- action_checkservice
	- slot{"requested_slot": "servicename"}
* inform{"servicename": "accenture"}
	- action_checkservice
	- slot{"servicename": "accenture"}

## CHECK SERVICE
*check_service
	- action_checkservice
	- slot{"requested_slot": "servicename"}
* inform{"servicename": "cnbc"}
	- action_checkservice
	- slot{"servicename": "cnbc"}
	
## CHECK SERVICE
*check_service
	- action_checkservice
	- slot{"requested_slot": "servicename"}
* inform{"servicename": "travelers"}
	- action_checkservice
	- slot{"servicename": "travelers"}

## CHECK SERVICE
*check_service
	- action_checkservice
	- slot{"requested_slot": "servicename"}
* inform{"servicename": "yahoo"}
	- action_checkservice
	- slot{"servicename": "yahoo"}
	
	
## CHECK SERVICE
*check_service{"servicename": "google"}
	- action_checkservice








##NEW STORY
* request_restaurant
     - action_search_restaurants
     - slot{"requested_slot": "cuisine"}
* inform{"cuisine": "chinese"}
     - action_search_restaurants
     - slot{"cuisine": "chinese"}
     - slot{"requested_slot": "people"}
* inform{"people": 3}
   - action_search_restaurants
