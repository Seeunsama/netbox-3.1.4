from rest_framework import serializers

from ipam import models
from netbox.api import WritableNestedSerializer

__all__ = [
    'NestedAggregateSerializer',
    'NestedASNSerializer',
    'NestedFHRPGroupSerializer',
    'NestedFHRPGroupAssignmentSerializer',
    'NestedIPAddressSerializer',
    'NestedIPRangeSerializer',
    'NestedPrefixSerializer',
    'NestedRIRSerializer',
    'NestedRoleSerializer',
    'NestedRouteTargetSerializer',
    'NestedServiceSerializer',
    'NestedVLANGroupSerializer',
    'NestedVLANSerializer',
    'NestedVRFSerializer',
]


#
# ASNs
#

class NestedASNSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:asn-detail')

    class Meta:
        model = models.ASN
        fields = ['id', 'url', 'display', 'asn']


#
# VRFs
#

class NestedVRFSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:vrf-detail')
    prefix_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.VRF
        fields = ['id', 'url', 'display', 'name', 'rd', 'prefix_count']


#
# Route targets
#

class NestedRouteTargetSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:routetarget-detail')

    class Meta:
        model = models.RouteTarget
        fields = ['id', 'url', 'display', 'name']


#
# RIRs/aggregates
#

class NestedRIRSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:rir-detail')
    aggregate_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.RIR
        fields = ['id', 'url', 'display', 'name', 'slug', 'aggregate_count']


class NestedAggregateSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:aggregate-detail')
    family = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Aggregate
        fields = ['id', 'url', 'display', 'family', 'prefix']


#
# FHRP groups
#

class NestedFHRPGroupSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:fhrpgroup-detail')

    class Meta:
        model = models.FHRPGroup
        fields = ['id', 'url', 'display', 'protocol', 'group_id']


class NestedFHRPGroupAssignmentSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:fhrpgroupassignment-detail')

    class Meta:
        model = models.FHRPGroupAssignment
        fields = ['id', 'url', 'display', 'interface_type', 'interface_id', 'group_id', 'priority']


#
# VLANs
#

class NestedRoleSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:role-detail')
    prefix_count = serializers.IntegerField(read_only=True)
    vlan_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Role
        fields = ['id', 'url', 'display', 'name', 'slug', 'prefix_count', 'vlan_count']


class NestedVLANGroupSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:vlangroup-detail')
    vlan_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.VLANGroup
        fields = ['id', 'url', 'display', 'name', 'slug', 'vlan_count']


class NestedVLANSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:vlan-detail')

    class Meta:
        model = models.VLAN
        fields = ['id', 'url', 'display', 'vid', 'name']


#
# Prefixes
#

class NestedPrefixSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:prefix-detail')
    family = serializers.IntegerField(read_only=True)
    _depth = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.Prefix
        fields = ['id', 'url', 'display', 'family', 'prefix', '_depth']


#
# IP ranges
#

class NestedIPRangeSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:iprange-detail')
    family = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.IPRange
        fields = ['id', 'url', 'display', 'family', 'start_address', 'end_address']


#
# IP addresses
#

class NestedIPAddressSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:ipaddress-detail')
    family = serializers.IntegerField(read_only=True)

    class Meta:
        model = models.IPAddress
        fields = ['id', 'url', 'display', 'family', 'address']


#
# Services
#

class NestedServiceSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='ipam-api:service-detail')

    class Meta:
        model = models.Service
        fields = ['id', 'url', 'display', 'name', 'protocol', 'ports']