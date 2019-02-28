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
* greet
    - utter_greet
* trigger_jenkinsjob
    - action_jenkins

## trigger_jenkinsjob_withjob
* trigger_jenkinsjob_withjob{"jenkinsjob": "sampleapp_ppl"}
    - action_jenkins
* bye
    - utter_anythingelse
	
## trigger_deploy
* trigger_deploy
	- utter_ask_appname
	- utter_ask_environment
* anythingelse
    - utter_anythingelse

## trigger_deploy_withapp
* trigger_deploy_withapp{"appname": "sampleapp"}
    - action_jenkins_param
* anythingelse
    - utter_anythingelse
		
## check_status_withID1
* check_JIRA_Status{"JIRAID": "TS-3"}
    - action_GetJIRAStatus_param
	
## check_jira_request1
* create_JIRA_request
    - action_createJIRArequest_param
		
## check_service_withservice1
* check_service_withservice{"servicename": "google"}
    - action_checkservice
* anythingelse
    - utter_anythingelse
