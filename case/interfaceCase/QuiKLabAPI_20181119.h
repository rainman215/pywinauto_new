/*!
 * \file QuiKLabAPI.h
 * \brief quiklab3.0�Ľӿڡ��ɹ���ͬ���Ե��á�
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

/// \details �źŽ��ջص��������Ͷ���
typedef int (__stdcall * OnSignalInputCallBackPtr)(const char signalName[], void* userParam);

/// \details �������ջص��������Ͷ���
typedef int (__stdcall * OnSignalParamInputCallBackPtr)(const char signalName[], const char paramName[], const double dValue, void* userParam);

/// \details ����ʱ�������»ص��������Ͷ���
typedef int (__stdcall * OnTestCaseRuntimeParamUpdateCallBackPtr)(const char paramName[], const double dValue, void* userParam);

typedef int API_RESULT; ///< \details 0 : SUCCESS   -1 : FAIL

#define RESULT_SUCESS	0	///< \details ����ɹ�
#define RESULT_FAIL		-1	///< \details ����ʧ��

//ƽ̨�빤�̵Ĳ���API
///////////////////////////////////////////////////////////////////////

/// \details ��ʼ��QuiKLabƽ̨��
API_RESULT API_EXPORT initQuiKLabPlatform();

/// \details �ͷ�ƽ̨��
API_RESULT API_EXPORT releaseQuiKLabPlatform();

/// \details ��ȡƽ̨����״̬
/// \retval -1 �쳣
/// \retval 0 ֹͣ
/// \retval 1 ����
int API_EXPORT getPlatformState();

/// \details ��ȡ��λ������
/// \retval < 0 �쳣
/// \retval >= 0 ����ֵ
int API_EXPORT getTargetCount();

/// \details ����������ȡ��λ��IP
/// \param[in] ntargetIndex ��λ������
/// \param[out] pOutBuffer ���ڴ����λ��ip�Ļ���ָ��
/// \param[in] outBufferSize ����Ĵ�С
API_RESULT API_EXPORT getTargetIP(int ntargetIndex, char pOutBuffer[], int outBufferSize);

/// \details ����������ȡ��λ��״̬
/// \retval -1 �쳣
/// \retval 0 ֹͣ
/// \retval 1 ����
API_RESULT API_EXPORT getTargetState(int ntargetIndex);

/// \details ����ʹ���е�Ŀ���IP,Ϊ��ʱ����Ϊ����ip
/// \param[in] pTargetIp Ŀ���ip�����������������е���λ��
API_RESULT API_EXPORT useTargetIp(const char pTargetIp[]);

/// \details ��ȡ��ǰƽ̨�Ĺ�������
/// \retval < 0 �쳣
/// \retval >= 0 ��������
int API_EXPORT getProjectCount();

/// \details ��ȡ��������
/// \param[in] nindex ��������
/// \param[out] pOutBuffer ���ڴ�Ź������Ļ���ָ��
/// \param[in] outBufferSize ����Ĵ�С
API_RESULT API_EXPORT getProjectName(int nindex, char pOutBuffer[], int outBufferSize);

/// \details ���ع���
/// \param[in] pProjectName ��Ź������Ļ���ָ��
API_RESULT API_EXPORT loadProject(const char pProjectName[]);

/// \details ж�ع���
/// \return ж�ؽ������Ŀδ���ػ�������ִ�����������ʱ����ж��ʧ��
API_RESULT API_EXPORT unLoadProject();

/// \details ��ȡ��ǰ���̵�����
/// \param[out] pOutBuffer ���ڴ�ŵ�ǰ�������Ļ���ָ��
/// \param[in] outBufferSize ����Ĵ�С
API_RESULT API_EXPORT getCurrentProjectName(char pOutBuffer[], int outBufferSize);

/// \details ��ȡip�Ƿ�����
/// \retval 1 ����
/// \retval 0 ������
int API_EXPORT getIpState(char pIp[]);

/// \details ����Ӳ����Դ��Ϣ
API_RESULT API_EXPORT updateInterfInfos();

/// \details ����ip��ȡ�忨���͸���
/// \param[in] pIp ip��ַ
/// \pre updateInterfInfos
/// \sa updateInterfInfos
int API_EXPORT getInterfNumFromIp(char pIp[]);

/// \details ����ip�Ͱ忨������ȡ�忨������Ϣ
/// \param[in] pIp ip��ַ
/// \param[in] interfIndex �忨����
/// \param[out] pInterfName ���ڴ�Ű忨���Ļ���ָ��
/// \param[in] interfNameLen �忨������Ĵ�С
/// \param[out] pInfo ���ڴ����Ϣ�Ļ���ָ��
/// \param[in] infoLen ��Ϣ����Ĵ�С
API_RESULT API_EXPORT getInterfInfo(char pIp[], int interfIndex, char pInterfName[], int interfNameLen, char pInfo[], int infoLen);


//������������������/ֹͣ
////////////////////////////////////////////////////////////////////////

/// \details ��ȡ��ǰ���̵Ĳ���������������
/// \retval < 0 �쳣
/// \retval >= 0 ����ֵ
int API_EXPORT  getTestCaseClassCount();

/// \details ������������ȡ��ǰ���̵Ĳ�������������
/// \param[in] TestCaseClassIndex ����������
/// \param[out] pOutBuffer ���ڴ�����������Ļ���ָ��
/// \param[in] outBufferSize ����Ĵ�С
API_RESULT API_EXPORT  getTestCaseClassName(int TestCaseClassIndex,char pOutBuffer[], int outBufferSize);

/// \details ��ȡ�����������Ĳ�����������
/// \param[in] pTestCaseClassName ��������
/// \retval < 0 �쳣
/// \retval >= 0 ����ֵ
int API_EXPORT getTestCaseCount(const char pTestCaseClassName[]);

/// \details ������������ȡ�����µĲ�����������
/// \param[in] pTestCaseClassName ��������
/// \param[in] TestCaseIndex ��������
/// \param[out] pOutBuffer ���ڴ���������Ļ���ָ��
/// \param[in] outBufferSize ����Ĵ�С
API_RESULT API_EXPORT getTestCaseName(const char pTestCaseClassName[], int TestCaseIndex, char pOutBuffer[], int outBufferSize);

/// \details ����ʹ���еĲ�������
/// \param[in] pTestCaseClassName ��������
/// \param[in] pTestCaseName ������
API_RESULT API_EXPORT useTestCase(const char pTestCaseClassName[], const char pTestCaseName[]);

/// \details Ϊ��ǰ����������������
/// \param[in] pTestName ���Լ�¼�����������ɲ��Լ�¼������
/// \return �����������
/// \pre ���ȵ���useTestCase��ȷ��ִ���ĸ�����
/// \sa useTestCase
API_RESULT API_EXPORT  startTestCase(const char pTestName[]);

/// \details ֹͣ��ǰ���̵Ĳ�������
API_RESULT API_EXPORT  stopTestCase();


//�����������������/ֹͣ
////////////////////////////////////////////////////////////////////////

/// \details ��ȡ��ǰ���̵Ĳ��������������
/// \retval < 0 �쳣
/// \retval >= 0 ����ֵ
int API_EXPORT  getTestTaskClassCount();

//������������ȡ��ǰ���̵Ĳ��������������
API_RESULT API_EXPORT  getTestTaskClassName(int TestTaskClassIndex,char pOutBuffer[], int outBufferSize);

/// \details ��ȡ�������񼯵Ĳ�����������
/// \param[in] pTestTaskClassName ������
/// \retval <0 �쳣
/// \retval >=0 ����ֵ
int API_EXPORT  getTestTaskCount(const char pTestTaskClassName[]);

/// \details ���������������������������ȡ������������
/// \param[in] pTestTaskClassName ����������
/// \param[in] TestTaskIndex ��������
/// \param[out] pOutBuffer ���ڴ���������Ļ���ָ��
/// \param[in] outBufferSize ����Ĵ�С
API_RESULT API_EXPORT getTestTaskName(const char pTestTaskClassName[], int TestTaskIndex, char pOutBuffer[], int outBufferSize);

/// \details ����ʹ���еĲ�������
/// \param[in] pTestTaskClassName ������
/// \param[in] pTestTaskName ������
API_RESULT API_EXPORT useTestTask(const char pTestTaskClassName[], const char pTestTaskName[]);

/// \details ��ȡ���������µĲ�����������
/// \pre ���ȵ���useTestTask
/// \sa useTestTask
int API_EXPORT getTestTaskTestCaseCount();

/// \details ����������������ȡ�����µĲ�����������
/// \param[in] TestCaseIndex ��������
/// \param[out] pOutBuffer ���ڴ���������Ļ���ָ��
/// \param[in] outBufferSize ����Ĵ�С
/// \pre ���ȵ���useTestTask
/// \sa useTestTask
API_RESULT API_EXPORT getTestTaskTestCaseName(int TestCaseIndex, char pOutBuffer[], int outBufferSize);

/// \details ����������������ȡ��ʼֵ������
/// \param[in] TestCaseIndex ��������
int API_EXPORT getTestTaskTestCaseDoubleCount(int TestCaseIndex);

/// \details �������������ͳ�ʼֵ��������ȡ��ʼֵ������ֵ
/// \param[in] TestCaseIndex ��������
/// \param[in] doubleIndex ��ʼֵ����
/// \param[out] pDoubleName ���ڴ�ų�ʼֵ���Ļ���ָ��
/// \param[in] doubleLen ����Ĵ�С
/// \param[out] doubleValue ���ڴ�ų�ʼֵ�Ļ���ָ��
API_RESULT API_EXPORT getTestTaskTestCaseDoubleNameValue(int TestCaseIndex, int doubleIndex, char pDoubleName[], int doubleLen, double *doubleValue);

/// \details �������������ͳ�ʼֵ���������ö�Ӧ��ʼֵ��ֵ
/// \param[in] TestCaseIndex ��������
/// \param[in] doubleIndex ��ʼֵ����
/// \param[in] doubleValue ��ʼֵ��ֵ
API_RESULT API_EXPORT setTestTaskTestCaseDoubleValue(int TestCaseIndex, int doubleIndex, double doubleValue);

/// \details ������������
/// \param[in] pTestName ���Լ�¼��
/// \pre useTestTask
/// \sa useTestTask
API_RESULT API_EXPORT startTestTask(const char pTestName[]);

/// \details ֹͣ��������
API_RESULT API_EXPORT stopTestTask();

/// \details ������������
/// \param[in] pTestTaskSetName ������
API_RESULT API_EXPORT startTestTaskSet(const char pTestTaskSetName[]);

/// \details ֹͣ��������
API_RESULT API_EXPORT stopTestTaskSet();

/// \details ���ò������񼯹�ѡ״̬��·��
/// \param[in] pTestTaskSetTablePath ״̬��·��
API_RESULT API_EXPORT updateTestTaskSetTablePath(const char pTestTaskSetTablePath[]);

//�Ե�ǰ���̵��źŹ���API
///////////////////////////////////////////////////////////////////////

/// \details ��ȡ���������źŵ�����
/// \retval < 0 �쳣
/// \retval >= 0 ����ֵ
int API_EXPORT  getInputSignalCount();

/// \details ��ȡ�����źŵ�����
/// \param[in] outputSignalIndex �����ź�����
/// \param[out] pOutBuffer ���ڴ���ź����Ļ���ָ��
/// \param[in] outBufferSize ����Ĵ�С
API_RESULT  API_EXPORT getInputSignalName(int inputSignalIndex,char pOutBuffer[], int outBufferSize);

/// \details ��ȡ��������źŵ�����
/// \retval < 0 �쳣
/// \retval >= 0 ����ֵ
int API_EXPORT  getOutputSignalCount();

/// \details ��ȡ����źŵ�����
/// \param[in] outputSignalIndex ����ź�����
/// \param[out] pOutBuffer ���ڴ���ź����Ļ���ָ��
/// \param[in] outBufferSize ����Ĵ�С
API_RESULT API_EXPORT getOutputSignalName(int outputSignalIndex, char pOutBuffer[], int outBufferSize);

/// \details ��ȡ�źŵĲ�������
/// \retval < 0 �쳣
/// \retval >= 0 ����ֵ
int API_EXPORT  getSignalParamCount(const char pSignalName[]);

/// \details ��ȡ�źŲ�������
/// \param[in] pSignalName �ź�����
/// \param[in] parmaIndex ��������
/// \param[out] pOutBuffer ���ڴ�Ų������Ļ���ָ��
/// \param[in] outBufferSize ����Ĵ�С
API_RESULT API_EXPORT  getSignalParamName(const char pSignalName[], int parmaIndex, char pOutBuffer[], int outBufferSize);


//�������ȡ�źŲ���API
////////////////////////////////////////////////////////////////////////////

/// \details �����Ƿ��ڻ�ȡ����ֵʱ�Զ����Ĳ�����Ĭ��Ϊtrue����ȡ����ֵʱ�Զ����Ĳ���
API_RESULT API_EXPORT setAutoRegWhenGetParamValue(bool bAutoReg);

/// \details ���������źŵĲ���
/// \param[in] pSignalName �ź���
/// \param[in] pParamName ������
API_RESULT API_EXPORT regInputSignalParam(const char pSignalName[], const char pParamName[]);

/// \details ȡ������
/// \param[in] pSignalName �ź���
/// \param[in] pParamName ������
API_RESULT API_EXPORT unRegInputSignalParam(const char pSignalName[], const char pParamName[]);

/// \details ��ȡ���ĵ��źŲ���ֵ
/// \param[in] pSignalName �ź���
/// \param[in] pParamName ������
double API_EXPORT getInputSignalParamValue(const char pSignalName[], const char pParamName[]);

/// \details �����ź�ֵ
/// \param[in] pSignalName �ź���
API_RESULT API_EXPORT resetInputSignal(const char pSignalName[]);

//�����ź�API
////////////////////////////////////////////////////////////////////////////
/// \details ���÷����źŵĲ���ֵ
/// \param[in] pSignalName �ź���
/// \param[in] pParamName ������
/// \param[in] dValue ����ֵ
API_RESULT API_EXPORT setOutputSignalParamValue(const char pSignalName[], const char pParamName[], double dValue);

/// \details ���÷��ͻ���
/// \param[in] pSignalName �ź���
API_RESULT API_EXPORT resetOutputSignal(const char pSignalName[]);

/// \details �����ź�
/// \param[in] pSignalName �ź���
API_RESULT API_EXPORT sendOutputSignal(const char pSignalName[]);


//��������������ʱ��������
//////////////////////////////////////////////////////////////////////////

/// \details ��ȡ������������ʱ�Ĳ�������
/// \retval < 0 �쳣
/// \retval >= 0 ����ֵ
int API_EXPORT getTestCaseRuntimeParamCount();

/// \details ��ȡ������������ʱ�Ĳ�������
/// \param[in] ��������
/// \param[out] ���ڲ����������Ļ���ָ��
/// \param[in] outBufferSize ����Ĵ�С
API_RESULT API_EXPORT getTestCaseRuntimeParamName(int nIndex, char pOutBuffer[], int outBufferSize);

/// \details ��ȡ������������ʱ�Ĳ���ֵ
/// \param[in] pParamName ������
/// \return ����ֵ
double API_EXPORT getTestCaseRuntimeParamValue(const char pParamName[]);

/// \details ���ò�����������ʱ����ֵ
/// \param[in] pParamName ������
/// \param[in] dValue ����ֵ
API_RESULT API_EXPORT setTestCaseRuntimeParamValue(const char pParamName[], double dValue);


//��ز��������������
//////////////////////////////////////////////////////////////////////////

/// \details �Ƿ�����ͣ״̬
/// \retval 0 ����ͣ״̬
/// \retval 1 ��ͣ״̬
/// \retval -1 �쳣
int API_EXPORT getStatusIsPause();

/// \details ���������Ƿ�������״̬
/// \retval 0 ֹͣ״̬
/// \retval 1 ����״̬״̬
int API_EXPORT getStatusForTestCaseRunning();

/// \details ������ͣ״̬
/// \param[in] pause ��ͣ��־��1����ͣ��0������ͣ
API_RESULT API_EXPORT setStatusIsPause(int pause);

/// \details ��ȡִ���еĲ�����������
/// \param[in] pTestTaskName ������
int API_EXPORT getStatusExcTestCaseCount(char pTestTaskName[]);

/// \details ����������ȡִ���еĲ�������������
/// \param[in] pTestTaskName ������
/// \param[in] nindex ��������
/// \param[out] pOutBuffer ���ڴ���������Ļ���ָ��
/// \param[in] outBufferSize ����Ĵ�С
API_RESULT API_EXPORT getStatusTestCaseName(char pTestTaskName[], int nindex, char pOutBuffer[], int outBufferSize);

/// \details ����������ȡִ���еĲ�������״̬
/// \retval 0 �ȴ�ִ��
/// \return 1 ����ִ��
/// \return 2 ִ�гɹ�
/// \return 3 ִ��ʧ��
/// \return -1 �쳣
int API_EXPORT getStatusForExcTestCase(char pTestTaskName[], int nindex);

/// \details �������������Ϣ
/// \param[in] pDir: ·���ַ���
/// \param[in] pProjectName: ������
API_RESULT API_EXPORT exportTestCaseInfo(char pDir[], char pProjectName[]);

/// \details ע��ص�����
/// \sa OnSignalInputCallBackPtr, OnSignalParamInputCallBackPtr, OnTestCaseRuntimeParamUpdateCallBackPtr
API_RESULT API_EXPORT regCallBack(
	OnSignalInputCallBackPtr sip,
	OnSignalParamInputCallBackPtr spip,
	OnTestCaseRuntimeParamUpdateCallBackPtr trp,
	void* userParam);
};

#endif // API_H
