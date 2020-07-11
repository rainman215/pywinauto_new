/*!
 * \file QuiKLabAPI.h
 * \brief quiklab3.0的接口。可供不同语言调用。
 * \date 2018/11/17
 */
 
#ifndef API_H
#define API_H

#ifdef QUIKLABAPI_LIB
# define API_EXPORT  __declspec(dllexport)
#else
# define API_EXPORT  __declspec(dllimport)
#endif

extern "C"
{

/// \details 信号接收回调函数类型定义
typedef int (__stdcall * OnSignalInputCallBackPtr)(const char signalName[], void* userParam);

/// \details 参数接收回调函数类型定义
typedef int (__stdcall * OnSignalParamInputCallBackPtr)(const char signalName[], const char paramName[], const double dValue, void* userParam);

/// \details 运行时参数更新回调函数类型定义
typedef int (__stdcall * OnTestCaseRuntimeParamUpdateCallBackPtr)(const char paramName[], const double dValue, void* userParam);

typedef int API_RESULT; ///< \details 0 : SUCCESS   -1 : FAIL

#define RESULT_SUCESS	0	///< \details 代表成功
#define RESULT_FAIL		-1	///< \details 代表失败

//平台与工程的操作API
///////////////////////////////////////////////////////////////////////

/// \details 初始化QuiKLab平台类
API_RESULT API_EXPORT initQuiKLabPlatform();

/// \details 释放平台类
API_RESULT API_EXPORT releaseQuiKLabPlatform();

/// \details 获取平台运行状态
/// \retval -1 异常
/// \retval 0 停止
/// \retval 1 运行
int API_EXPORT getPlatformState();

/// \details 获取下位机数量
/// \retval < 0 异常
/// \retval >= 0 数量值
int API_EXPORT getTargetCount();

/// \details 根据索引获取下位机IP
/// \param[in] ntargetIndex 下位机索引
/// \param[out] pOutBuffer 用于存放下位机ip的缓存指针
/// \param[in] outBufferSize 缓存的大小
API_RESULT API_EXPORT getTargetIP(int ntargetIndex, char pOutBuffer[], int outBufferSize);

/// \details 根据索引获取下位机状态
/// \retval -1 异常
/// \retval 0 停止
/// \retval 1 运行
API_RESULT API_EXPORT getTargetState(int ntargetIndex);

/// \details 设置使用中的目标机IP,为空时设置为本机ip
/// \param[in] pTargetIp 目标机ip，包括本机与网络中的下位机
API_RESULT API_EXPORT useTargetIp(const char pTargetIp[]);

/// \details 获取当前平台的工程数量
/// \retval < 0 异常
/// \retval >= 0 工程数量
int API_EXPORT getProjectCount();

/// \details 获取工程名称
/// \param[in] nindex 工程索引
/// \param[out] pOutBuffer 用于存放工程名的缓存指针
/// \param[in] outBufferSize 缓存的大小
API_RESULT API_EXPORT getProjectName(int nindex, char pOutBuffer[], int outBufferSize);

/// \details 加载工程
/// \param[in] pProjectName 存放工程名的缓存指针
API_RESULT API_EXPORT loadProject(const char pProjectName[]);

/// \details 卸载工程
/// \return 卸载结果。项目未加载或者正在执行用例等情况时，则卸载失败
API_RESULT API_EXPORT unLoadProject();

/// \details 获取当前工程的名称
/// \param[out] pOutBuffer 用于存放当前工程名的缓存指针
/// \param[in] outBufferSize 缓存的大小
API_RESULT API_EXPORT getCurrentProjectName(char pOutBuffer[], int outBufferSize);

/// \details 获取ip是否在线
/// \retval 1 在线
/// \retval 0 不在线
int API_EXPORT getIpState(char pIp[]);

/// \details 更新硬件资源信息
API_RESULT API_EXPORT updateInterfInfos();

/// \details 根据ip获取板卡类型个数
/// \param[in] pIp ip地址
/// \pre updateInterfInfos
/// \sa updateInterfInfos
int API_EXPORT getInterfNumFromIp(char pIp[]);

/// \details 根据ip和板卡索引获取板卡名和信息
/// \param[in] pIp ip地址
/// \param[in] interfIndex 板卡索引
/// \param[out] pInterfName 用于存放板卡名的缓存指针
/// \param[in] interfNameLen 板卡名缓存的大小
/// \param[out] pInfo 用于存放信息的缓存指针
/// \param[in] infoLen 信息缓存的大小
API_RESULT API_EXPORT getInterfInfo(char pIp[], int interfIndex, char pInterfName[], int interfNameLen, char pInfo[], int infoLen);


//测试用例管理与启动/停止
////////////////////////////////////////////////////////////////////////

/// \details 获取当前工程的测试用例分类数量
/// \retval < 0 异常
/// \retval >= 0 数量值
int API_EXPORT  getTestCaseClassCount();

/// \details 根据索引，获取当前工程的测试用例集名称
/// \param[in] TestCaseClassIndex 用例集索引
/// \param[out] pOutBuffer 用于存放用例集名的缓存指针
/// \param[in] outBufferSize 缓存的大小
API_RESULT API_EXPORT  getTestCaseClassName(int TestCaseClassIndex,char pOutBuffer[], int outBufferSize);

/// \details 获取测试用例集的测试用例数量
/// \param[in] pTestCaseClassName 用例集名
/// \retval < 0 异常
/// \retval >= 0 数量值
int API_EXPORT getTestCaseCount(const char pTestCaseClassName[]);

/// \details 根据索引，获取分类下的测试用例名称
/// \param[in] pTestCaseClassName 用例集名
/// \param[in] TestCaseIndex 用例索引
/// \param[out] pOutBuffer 用于存放用例名的缓存指针
/// \param[in] outBufferSize 缓存的大小
API_RESULT API_EXPORT getTestCaseName(const char pTestCaseClassName[], int TestCaseIndex, char pOutBuffer[], int outBufferSize);

/// \details 设置使用中的测试用例
/// \param[in] pTestCaseClassName 用例集名
/// \param[in] pTestCaseName 用例名
API_RESULT API_EXPORT useTestCase(const char pTestCaseClassName[], const char pTestCaseName[]);

/// \details 为当前工程启动测试用例
/// \param[in] pTestName 测试记录名，用于生成测试记录的名称
/// \return 用例启动结果
/// \pre 需先调用useTestCase以确定执行哪个用例
/// \sa useTestCase
API_RESULT API_EXPORT  startTestCase(const char pTestName[]);

/// \details 停止当前工程的测试用例
API_RESULT API_EXPORT  stopTestCase();


//测试任务管理与启动/停止
////////////////////////////////////////////////////////////////////////

/// \details 获取当前工程的测试任务分类数量
/// \retval < 0 异常
/// \retval >= 0 数量值
int API_EXPORT  getTestTaskClassCount();

//根据索引，获取当前工程的测试任务分类名称
API_RESULT API_EXPORT  getTestTaskClassName(int TestTaskClassIndex,char pOutBuffer[], int outBufferSize);

/// \details 获取测试任务集的测试任务数量
/// \param[in] pTestTaskClassName 任务集名
/// \retval <0 异常
/// \retval >=0 数量值
int API_EXPORT  getTestTaskCount(const char pTestTaskClassName[]);

/// \details 根据任务分类名和任务索引，获取测试任务名称
/// \param[in] pTestTaskClassName 用例任务集名
/// \param[in] TestTaskIndex 任务索引
/// \param[out] pOutBuffer 用于存放任务名的缓存指针
/// \param[in] outBufferSize 缓存的大小
API_RESULT API_EXPORT getTestTaskName(const char pTestTaskClassName[], int TestTaskIndex, char pOutBuffer[], int outBufferSize);

/// \details 设置使用中的测试任务
/// \param[in] pTestTaskClassName 任务集名
/// \param[in] pTestTaskName 任务名
API_RESULT API_EXPORT useTestTask(const char pTestTaskClassName[], const char pTestTaskName[]);

/// \details 获取测试任务下的测试用例数量
/// \pre 需先调用useTestTask
/// \sa useTestTask
int API_EXPORT getTestTaskTestCaseCount();

/// \details 根据用例索引，获取任务下的测试用例名称
/// \param[in] TestCaseIndex 用例索引
/// \param[out] pOutBuffer 用于存放用例名的缓存指针
/// \param[in] outBufferSize 缓存的大小
/// \pre 需先调用useTestTask
/// \sa useTestTask
API_RESULT API_EXPORT getTestTaskTestCaseName(int TestCaseIndex, char pOutBuffer[], int outBufferSize);

/// \details 根据用例索引，获取初始值的数量
/// \param[in] TestCaseIndex 用例索引
int API_EXPORT getTestTaskTestCaseDoubleCount(int TestCaseIndex);

/// \details 根据用例索引和初始值索引，获取初始值的名和值
/// \param[in] TestCaseIndex 用例索引
/// \param[in] doubleIndex 初始值索引
/// \param[out] pDoubleName 用于存放初始值名的缓存指针
/// \param[in] doubleLen 缓存的大小
/// \param[out] doubleValue 用于存放初始值的缓存指针
API_RESULT API_EXPORT getTestTaskTestCaseDoubleNameValue(int TestCaseIndex, int doubleIndex, char pDoubleName[], int doubleLen, double *doubleValue);

/// \details 根据用例索引和初始值索引，设置对应初始值的值
/// \param[in] TestCaseIndex 用例索引
/// \param[in] doubleIndex 初始值索引
/// \param[in] doubleValue 初始值的值
API_RESULT API_EXPORT setTestTaskTestCaseDoubleValue(int TestCaseIndex, int doubleIndex, double doubleValue);

/// \details 启动测试任务
/// \param[in] pTestName 测试记录名
/// \pre useTestTask
/// \sa useTestTask
API_RESULT API_EXPORT startTestTask(const char pTestName[]);

/// \details 停止测试任务
API_RESULT API_EXPORT stopTestTask();

/// \details 启动测试任务集
/// \param[in] pTestTaskSetName 任务集名
API_RESULT API_EXPORT startTestTaskSet(const char pTestTaskSetName[]);

/// \details 停止测试任务集
API_RESULT API_EXPORT stopTestTaskSet();

/// \details 设置测试任务集勾选状态表路径
/// \param[in] pTestTaskSetTablePath 状态表路径
API_RESULT API_EXPORT updateTestTaskSetTablePath(const char pTestTaskSetTablePath[]);

//对当前工程的信号管理API
///////////////////////////////////////////////////////////////////////

/// \details 获取工程输入信号的数量
/// \retval < 0 异常
/// \retval >= 0 数量值
int API_EXPORT  getInputSignalCount();

/// \details 获取输入信号的名称
/// \param[in] outputSignalIndex 输入信号索引
/// \param[out] pOutBuffer 用于存放信号名的缓存指针
/// \param[in] outBufferSize 缓存的大小
API_RESULT  API_EXPORT getInputSignalName(int inputSignalIndex,char pOutBuffer[], int outBufferSize);

/// \details 获取工程输出信号的数量
/// \retval < 0 异常
/// \retval >= 0 数量值
int API_EXPORT  getOutputSignalCount();

/// \details 获取输出信号的名称
/// \param[in] outputSignalIndex 输出信号索引
/// \param[out] pOutBuffer 用于存放信号名的缓存指针
/// \param[in] outBufferSize 缓存的大小
API_RESULT API_EXPORT getOutputSignalName(int outputSignalIndex, char pOutBuffer[], int outBufferSize);

/// \details 获取信号的参数数量
/// \retval < 0 异常
/// \retval >= 0 数量值
int API_EXPORT  getSignalParamCount(const char pSignalName[]);

/// \details 获取信号参数名称
/// \param[in] pSignalName 信号索引
/// \param[in] parmaIndex 参数索引
/// \param[out] pOutBuffer 用于存放参数名的缓存指针
/// \param[in] outBufferSize 缓存的大小
API_RESULT API_EXPORT  getSignalParamName(const char pSignalName[], int parmaIndex, char pOutBuffer[], int outBufferSize);


//订阅与获取信号参数API
////////////////////////////////////////////////////////////////////////////

/// \details 设置是否在获取参数值时自动订阅参数，默认为true即获取参数值时自动订阅参数
API_RESULT API_EXPORT setAutoRegWhenGetParamValue(bool bAutoReg);

/// \details 订阅输入信号的参数
/// \param[in] pSignalName 信号名
/// \param[in] pParamName 参数名
API_RESULT API_EXPORT regInputSignalParam(const char pSignalName[], const char pParamName[]);

/// \details 取消订阅
/// \param[in] pSignalName 信号名
/// \param[in] pParamName 参数名
API_RESULT API_EXPORT unRegInputSignalParam(const char pSignalName[], const char pParamName[]);

/// \details 获取订阅的信号参数值
/// \param[in] pSignalName 信号名
/// \param[in] pParamName 参数名
double API_EXPORT getInputSignalParamValue(const char pSignalName[], const char pParamName[]);

/// \details 重置信号值
/// \param[in] pSignalName 信号名
API_RESULT API_EXPORT resetInputSignal(const char pSignalName[]);

//发送信号API
////////////////////////////////////////////////////////////////////////////
/// \details 设置发送信号的参数值
/// \param[in] pSignalName 信号名
/// \param[in] pParamName 参数名
/// \param[in] dValue 参数值
API_RESULT API_EXPORT setOutputSignalParamValue(const char pSignalName[], const char pParamName[], double dValue);

/// \details 重置发送缓存
/// \param[in] pSignalName 信号名
API_RESULT API_EXPORT resetOutputSignal(const char pSignalName[]);

/// \details 发送信号
/// \param[in] pSignalName 信号名
API_RESULT API_EXPORT sendOutputSignal(const char pSignalName[]);


//测试用例的运行时参数控制
//////////////////////////////////////////////////////////////////////////

/// \details 获取测试用例运行时的参数数量
/// \retval < 0 异常
/// \retval >= 0 数量值
int API_EXPORT getTestCaseRuntimeParamCount();

/// \details 获取测试用例运行时的参数名称
/// \param[in] 参数索引
/// \param[out] 用于参数参数名的缓存指针
/// \param[in] outBufferSize 缓存的大小
API_RESULT API_EXPORT getTestCaseRuntimeParamName(int nIndex, char pOutBuffer[], int outBufferSize);

/// \details 获取测试用例运行时的参数值
/// \param[in] pParamName 参数名
/// \return 参数值
double API_EXPORT getTestCaseRuntimeParamValue(const char pParamName[]);

/// \details 设置测试用例运行时参数值
/// \param[in] pParamName 参数名
/// \param[in] dValue 参数值
API_RESULT API_EXPORT setTestCaseRuntimeParamValue(const char pParamName[], double dValue);


//监控测试用例运行情况
//////////////////////////////////////////////////////////////////////////

/// \details 是否处于暂停状态
/// \retval 0 非暂停状态
/// \retval 1 暂停状态
/// \retval -1 异常
int API_EXPORT getStatusIsPause();

/// \details 测试用例是否处于运行状态
/// \retval 0 停止状态
/// \retval 1 运行状态状态
int API_EXPORT getStatusForTestCaseRunning();

/// \details 设置暂停状态
/// \param[in] pause 暂停标志。1：暂停；0：不暂停
API_RESULT API_EXPORT setStatusIsPause(int pause);

/// \details 获取执行中的测试用例个数
/// \param[in] pTestTaskName 任务名
int API_EXPORT getStatusExcTestCaseCount(char pTestTaskName[]);

/// \details 根据索引获取执行中的测试用例的名称
/// \param[in] pTestTaskName 任务名
/// \param[in] nindex 用例索引
/// \param[out] pOutBuffer 用于存放用例名的缓存指针
/// \param[in] outBufferSize 缓存的大小
API_RESULT API_EXPORT getStatusTestCaseName(char pTestTaskName[], int nindex, char pOutBuffer[], int outBufferSize);

/// \details 根据索引获取执行中的测试用例状态
/// \retval 0 等待执行
/// \return 1 正在执行
/// \return 2 执行成功
/// \return 3 执行失败
/// \return -1 异常
int API_EXPORT getStatusForExcTestCase(char pTestTaskName[], int nindex);

/// \details 导出用例相关信息
/// \param[in] pDir: 路径字符串
/// \param[in] pProjectName: 工程名
API_RESULT API_EXPORT exportTestCaseInfo(char pDir[], char pProjectName[]);

/// \details 注册回调函数
/// \sa OnSignalInputCallBackPtr, OnSignalParamInputCallBackPtr, OnTestCaseRuntimeParamUpdateCallBackPtr
API_RESULT API_EXPORT regCallBack(
	OnSignalInputCallBackPtr sip,
	OnSignalParamInputCallBackPtr spip,
	OnTestCaseRuntimeParamUpdateCallBackPtr trp,
	void* userParam);
};

#endif // API_H
