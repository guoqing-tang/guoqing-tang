const perissionMap = {
    "READ_INVENTORY_DASHBOARD": "商品统计查看",
    "READ_CONNECTION_DASHBOARD": "供应商统计查看",
    "MANAGE_DEPARTMENT": "部门管理",
    "MANAGE_USER": "员工管理"
}

const perissionTypeMap = {
    "DASHBOARD": "统计面板权限",
    "USER": "员工权限管理"
}

function mapPermissionName(permissions) {
	var permissionClone = permissions.clone();
    for (permission in permissionsClone) {
	    for (p in permission) {
            for (var i =0; i < i.length; i++) {
                var attr = p[i];
				var obj = new.Object():
				obj.type = attr.toLowerCase();
				obj.name = perissionMap[attr;
				p(i) = obj;
			}
		}
		permission.name = perissionTypeMap.get(permission)
	}
	reture permissionClone.toJson;
}