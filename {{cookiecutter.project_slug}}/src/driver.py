from cloudshell.cp.core import DriverRequestParser
from cloudshell.shell.core.resource_driver_interface import ResourceDriverInterface
from cloudshell.cp.core.models import DriverResponse
from cloudshell.shell.core.driver_context import InitCommandContext, AutoLoadCommandContext, ResourceCommandContext, \
    AutoLoadAttribute, AutoLoadDetails, CancellationContext, ResourceRemoteCommandContext


#from data_model import *  # run 'shellfoundry generate' to generate data model classes

class {{cookiecutter.driver_name}} (ResourceDriverInterface):

    def __init__(self):
        """
        ctor must be without arguments, it is created with reflection at run time
        """
        self.request_parser = DriverRequestParser()

    def initialize(self, context):
        """
        Called every time a new instance of the driver is created

        This method can be left unimplemented but this is a good place to load and cache the driver configuration,
        initiate sessions etc.
        Whatever you choose, do not remove it.

        :param InitCommandContext context: the context the command runs on
        """
        pass

    # <editor-fold desc="Mandatory Commands">

    # <editor-fold desc="Discovery">

    def get_inventory(self, context):
        """
        Called when the cloud provider resource is created
        in the inventory.

        Method validates the values of the cloud provider attributes, entered by the user as part of the cloud provider resource creation.
        In addition, this would be the place to assign values programmatically to optional attributes that were not given a value by the user.

        If one of the validations failed, the method should raise an exception

        :param AutoLoadCommandContext context: the context the command runs on
        :return Attribute and sub-resource information for the Shell resource you can return an AutoLoadDetails object
        :rtype: AutoLoadDetails
        """

        # run 'shellfoundry generate' in order to create classes that represent your data model

        return AutoLoadDetails([], [])

    # </editor-fold>

    # <editor-fold desc="App Deployment">

    def Deploy(self, context, request, cancellation_context=None):
        """
        Called when reserving a sandbox during setup, a call for each app in the sandbox.

        Method creates the compute resource in the cloud provider - VM instance or container.

        If App deployment fails, return a "success false" action result.

        :param ResourceCommandContext context:
        :param str request: A JSON string with the list of requested deployment actions
        :param CancellationContext cancellation_context:
        :return:
        :rtype: str
        """

        '''
        # parse the json strings into action objects
        actions = self.request_parser.convert_driver_request_to_actions(request)
        
        # extract DeployApp action
        deploy_action = single(actions, lambda x: isinstance(x, DeployApp))
        
        # if we have multiple supported deployment options use the 'deploymentPath' property 
        # to decide which deployment option to use. 
        deployment_name = deploy_action.actionParams.deployment.deploymentPath
                
        deploy_result = _my_deploy_method(context, actions, cancellation_context)
        return DriverResponse(deploy_result).to_driver_response_json()
        '''
        pass

    def PowerOn(self, context, ports):
        """
        Called when reserving a sandbox during setup, a call for each app in the sandbox can also be run manually by the sandbox end-user from the deployed App's commands pane

        Method spins up the VM

        If the operation fails, method should raise an exception.

        :param ResourceRemoteCommandContext context:
        :param ports:
        """
        pass

    def remote_refresh_ip(self, context, ports, cancellation_context):
        """

        Called when reserving a sandbox during setup, a call for each app in the sandbox can also be run manually by the sandbox end-user from the deployed App's commands pane

        Method retrieves the VM's updated IP address from the cloud provider and sets it on the deployed App resource
        Both private and public IPs are retrieved, as appropriate.

        If the operation fails, method should raise an exception.

        :param ResourceRemoteCommandContext context:
        :param ports:
        :param CancellationContext cancellation_context:
        :return:
        """
        pass

    def GetVmDetails(self, context, requests, cancellation_context):
        """
        Called when reserving a sandbox during setup, a call for each app in the sandbox can also be run manually by the sandbox
        end-user from the deployed App's VM Details pane

        Method queries cloud provider for instance operating system, specifications and networking information and
        returns that as a json serialized driver response containing a list of VmDetailsData.

        If the operation fails, method should raise an exception.

        :param ResourceCommandContext context:
        :param str requests:
        :param CancellationContext cancellation_context:
        :return:
        """
        pass

    # </editor-fold>

    def PowerCycle(self, context, ports, delay):
        """ please leave it as is """
        pass

    # <editor-fold desc="Power off / Delete">

    def PowerOff(self, context, ports):
        """
        Called during sandbox's teardown can also be run manually by the sandbox end-user from the deployed App's commands pane

        Method shuts down (or powers off) the VM instance.

        If the operation fails, method should raise an exception.

        :param ResourceRemoteCommandContext context:
        :param ports:
        """
        pass

    def DeleteInstance(self, context, ports):
        """
        Called during sandbox's teardown or when removing a deployed App from the sandbox

        Method deletes the VM from the cloud provider.

        If the operation fails, method should raise an exception.

        :param ResourceRemoteCommandContext context:
        :param ports:
        """
        pass

    # </editor-fold>

    # </editor-fold>


    ### NOTE: According to the Connectivity Type of your shell, remove the commands that are not
    ###       relevant from this file and from drivermetadata.xml.

    # <editor-fold desc="Mandatory Commands For L2 Connectivity Type">

    def ApplyConnectivityChanges(self, context, request):
        """
        Called during the orchestration setup and also called in a live sandbox when
        and instance is connected or disconnected from a VLAN
        service or from another instance (P2P connection).

        Method connects/disconnect VMs to VLANs based on requested actions (SetVlan, RemoveVlan)
        It's recommended to follow the "get or create" pattern when implementing this method.

        If operation fails, return a "success false" action result.

        :param ResourceCommandContext context: The context object for the command with resource and reservation info
        :param str request: A JSON string with the list of requested connectivity changes
        :return: a json object with the list of connectivity changes which were carried out by the driver
        :rtype: str
        """
        pass

    # </editor-fold> 

    # <editor-fold desc="Mandatory Commands For L3 Connectivity Type">

    def PrepareSandboxInfra(self, context, request, cancellation_context):
        """
        Called in the beginning of the orchestration flow (preparation stage), even before Deploy is called.

        Prepares all of the required infrastructure needed for a sandbox operating with L3 connectivity.
        For example, creating networking infrastructure like VPC, subnets or routing tables in AWS, storage entities such as S3 buckets, or
        keyPair objects for authentication.
        In general, any other entities needed on the sandbox level should be created here.

        Note:
        PrepareSandboxInfra can be called multiple times in a sandbox.
        Setup can be called multiple times in the sandbox, and every time setup is called, the PrepareSandboxInfra method will be called again.
        Implementation should support this use case and take under consideration that the cloud resource might already exist.
        It's recommended to follow the "get or create" pattern when implementing this method.

        When an error is raised or method returns action result with success false
        Cloudshell will fail sandbox creation, so bear that in mind when doing so.

        :param ResourceCommandContext context:
        :param str request:
        :param CancellationContext cancellation_context:
        :return:
        :rtype: str
        """
        '''
        # parse the json strings into action objects
        actions = self.request_parser.convert_driver_request_to_actions(request)
        
        action_results = _my_prepare_connectivity(context, actions, cancellation_context)
        
        return DriverResponse(action_results).to_driver_response_json()    
        '''
        pass

    def CleanupSandboxInfra(self, context, request):
        """
        Called at the end of reservation teardown

        Cleans all entities (beside VMs) created for sandbox, usually entities created in the
        PrepareSandboxInfra command.

        Basically all created entities for the sandbox will be deleted by calling the methods: DeleteInstance, CleanupSandboxInfra

        If a failure occurs, return a "success false" action result.

        :param ResourceCommandContext context:
        :param str request:
        :return:
        :rtype: str
        """
        '''
        # parse the json strings into action objects
        actions = self.request_parser.convert_driver_request_to_actions(request)
        
        action_results = _my_cleanup_connectivity(context, actions)

        return DriverResponse(action_results).to_driver_response_json()    
        '''
        pass

    # </editor-fold>

    # <editor-fold desc="Optional Commands For L3 Connectivity Type">

    def SetAppSecurityGroups(self, context, request):
        """
        Called via cloudshell API call

        Programmatically set which ports will be open on each of the apps in the sandbox, and from
        where they can be accessed. This is an optional command that may be implemented.
        Normally, all outbound traffic from a deployed app should be allowed.
        For inbound traffic, we may use this method to specify the allowed traffic.
        An app may have several networking interfaces in the sandbox. For each such interface, this command allows to set
        which ports may be opened, the protocol and the source CIDR

        If operation fails, return a "success false" action result.

        :param ResourceCommandContext context:
        :param str request:
        :return:
        :rtype: str
        """
        pass

    # </editor-fold>

    def cleanup(self):
        """
        Destroy the driver session, this function is called every time a driver instance is destroyed
        This is a good place to close any open sessions, finish writing to log files, etc.
        """
        pass