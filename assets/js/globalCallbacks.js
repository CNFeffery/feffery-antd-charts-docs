window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        toggleSideMenuVisible: (nClicks, originIcon) => {
            if (originIcon === 'antd-arrow-left') {
                window.dash_clientside.set_props(
                    'toggle-side-menu-icon',
                    {
                        icon: 'antd-arrow-right'
                    }
                );
                window.dash_clientside.set_props(
                    'side-menu-affix',
                    {
                        style: {
                            width: 20
                        }
                    }
                );
                window.dash_clientside.set_props(
                    'side-menu-container',
                    {
                        style: {
                            opacity: 0
                        }
                    }
                );
            } else {
                window.dash_clientside.set_props(
                    'toggle-side-menu-icon',
                    {
                        icon: 'antd-arrow-left'
                    }
                );
                window.dash_clientside.set_props(
                    'side-menu-affix',
                    {
                        style: {
                            width: 325
                        }
                    }
                );
                window.dash_clientside.set_props(
                    'side-menu-container',
                    {
                        style: {
                            opacity: 1
                        }
                    }
                );
            }
        },
        handleMenuTargetScoll: (pathname) => {

            // 处理侧边菜单项滚动
            setTimeout(() => {
                // 查找当前页面中name为pathname的元素
                let scrollTarget = document.getElementsByName(pathname)
                if (scrollTarget.length > 0) {
                    // 滚动到该元素
                    scrollTarget[0].scrollIntoView({ behavior: "smooth" });
                }
            }, 1000)

        },
        toggleSidePropsVisible: (nClicks, originIcon) => {
            // 若先前处于显示状态
            if (originIcon === 'antd-arrow-right') {
                return [
                    {
                        width: 20
                    },
                    'antd-arrow-left'
                ]
            }

            return [
                {
                    width: 500
                },
                'antd-arrow-right'
            ]
        },
        toggleDemoCodeVisible: (nClicks, originStyle) => {
            // 若先前处于显示状态
            if (!originStyle?.display) {
                return {
                    display: 'none'
                }
            }
            return null;
        },
        toggleDocAnchorVisible: (nClicks, originIcon) => {
            // 若先前处于显示状态
            if (originIcon === 'antd-menu-unfold') {
                return [
                    {
                        width: 0,
                        display: 'none'
                    },
                    'antd-menu-fold'
                ]
            }

            return [
                {},
                'antd-menu-unfold'
            ]
        },
        smallScreenAutoCollapseSide: (responsive, nClicksLeft, nClicksRight, iconLeft, iconRight) => {
            // 满足较小屏幕尺寸规格要求
            if (!responsive?.lg) {
                return [
                    // 根据先前的导航菜单折叠状态，选择要更新的新状态
                    iconLeft === 'antd-arrow-left' ? (nClicksLeft || 0) + 1 : window.dash_clientside.no_update,
                    // 根据先前的侧边参数栏折叠状态，选择要更新的新状态
                    iconRight === 'antd-arrow-right' ? (nClicksRight || 0) + 1 : window.dash_clientside.no_update,
                    { display: 'none' },
                    { display: 'none' },
                    {}
                ]
            }
            return [
                window.dash_clientside.no_update,
                window.dash_clientside.no_update,
                {},
                {},
                { display: 'none' }
            ];
        },
        smallScreenUpdateHeader: (responsive) => {
            // 满足较小屏幕尺寸规格要求
            if (!responsive?.lg) {
                return [
                    { display: 'none' },
                    { display: 'none' },
                    {}
                ]
            }
            return [
                {},
                {},
                { display: 'none' }
            ];
        }
    }
});