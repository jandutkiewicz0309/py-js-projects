#include <iostream>
#include <windef.h>
#include <Wbemidl.h>
#pragma comment(lib, "wbemuuid.lib")

int main() {

    HRESULT hres = CoInitializeEx(0, COINIT_MULTITHREADED);
    if (FAILED(hres)) {
        std::cout << "Failed to initialize COM library." << std::endl;
        return 1;
    }

    hres = CoInitializeSecurity(
        NULL, -1, NULL, NULL,
        RPC_C_AUTHN_LEVEL_DEFAULT, 
        RPC_C_IMP_LEVEL_IMPERSONATE, 
        NULL, EOAC_NONE, NULL
    );
    if (FAILED(hres)) {
        std::cout << "Failed to initialize security." << std::endl;
        CoUninitialize();
        return 1;
    }

    IWbemLocator* pLocator = NULL;
    hres = CoCreateInstance(
        CLSID_WbemLocator, 0, CLSCTX_INPROC_SERVER,
        IID_IWbemLocator, (LPVOID*)&pLocator
    );
    if (FAILED(hres)) {
        std::cout << "Failed to create IWbemLocator object." << std::endl;
        CoUninitialize();
        return 1;
    }

    IWbemServices* pServices = NULL;
    hres = pLocator->ConnectServer(
        _bstr_t(L"ROOT\\CIMV2"), NULL, NULL, 0, NULL, 0, 0, &pServices
    );
    if (FAILED(hres)) {
        std::cout << "Could not connect to WMI." << std::endl;
        pLocator->Release();
        CoUninitialize();
        return 1;
    }

    IEnumWbemClassObject* pEnumerator = NULL;
    hres = pServices->ExecQuery(
        bstr_t("WQL"), 
        bstr_t("SELECT Name FROM Win32_Processor"),
        WBEM_FLAG_FORWARD_ONLY | WBEM_FLAG_RETURN_IMMEDIATELY, 
        NULL, 
        &pEnumerator
    );
    if (FAILED(hres)) {
        std::cout << "WMI Query Failed." << std::endl;
        pServices->Release();
        pLocator->Release();
        CoUninitialize();
        return 1;
    }

    IWbemClassObject* pclsObj = NULL;
    ULONG uReturn = 0;

    while (pEnumerator) {
        HRESULT hr = pEnumerator->Next(WBEM_INFINITE, 1, &pclsObj, &uReturn);
        if (0 == uReturn) break;

        VARIANT vtProp;
        hr = pclsObj->Get(L"Name", 0, &vtProp, 0, 0);
        std::wcout << "CPU Name : " << vtProp.bstrVal << std::endl;
        VariantClear(&vtProp);
        pclsObj->Release();
    }

    pServices->Release();
    pLocator->Release();
    pEnumerator->Release();
    CoUninitialize();
    return 0;
}
