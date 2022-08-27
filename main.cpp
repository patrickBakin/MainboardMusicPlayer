
#include <iostream>
#include <string>
#include <stdio.h>
#include <Windows.h>
#include <thread>
#include <chrono>
#include <ctime>  
#include "inpout32.h"
#include "ini.h"


void StopBeep()
{
    Out32(0x61, (Inp32(0x61) & 0xFC));
}

void beep(unsigned int freq, int ms)
{
    Out32(0x43, 0xB6);
    int div = 0x1234dc / freq;
    Out32(0x42, (div & 0xFF));
    Out32(0x42, (div >> 8));
    Sleep(10);
    Out32(0x61, (Inp32(0x61)) | 0x03);
    Sleep(ms);
    StopBeep();
}

BOOL WINAPI CtrlHandler(DWORD fdwCtrlType)
{
    switch (fdwCtrlType)
    {
        // Handle the CTRL-C signal.
    case CTRL_C_EVENT:
        printf("Ctrl-C event\n\n");
        
        StopBeep();
        exit(1);
        return TRUE;


    default:
        return FALSE;
    }
}

std::vector<std::string> explode(const std::string& str, const char& ch) {
    std::string next;
    std::vector<std::string> result;

    
    for (std::string::const_iterator it = str.begin(); it != str.end(); it++) {
        
        if (*it == ch) {
            
            if (!next.empty()) {
                
                result.push_back(next);
                next.clear();
            }
        }
        else {
            
            next += *it;
        }
    }
    if (!next.empty())
        result.push_back(next);
    return result;
}
void ExtSpeaker(std::chrono::system_clock::time_point timestart,std::vector<std::string> NoteL, std::vector<std::string> DurL, std::vector<std::string> StrtL, std::vector<std::string> StpL)
{
    int i = 0;
    std::chrono::system_clock::time_point start = timestart;
    std::cout << NoteL.size() << std::endl;
    while (i < NoteL.size())
    {
      
        std::chrono::duration<double> elapsed_seconds = std::chrono::system_clock::now() - start;
        if ((elapsed_seconds).count() >= stod(StrtL[i]))
        {
            
            Beep(static_cast<int>(stod(NoteL[i])), static_cast<int>(stod(DurL[i]) * 1000));
            i++;
        }


    }
}
int main()
{   


    mINI::INIFile file("Song.ini");
    mINI::INIStructure ini;
    file.read(ini);
    std::string& NotesR = ini["Song"]["NotesR"];
    std::string& DurationR = ini["Song"]["DurationR"];
    std::string& StartR = ini["Song"]["StartR"];
    std::string& StopR = ini["Song"]["StopR"];

    /*uncomment if you wish to use another speaker to provide Left-handed notes*/
   /* std::string& NotesL = ini["Song"]["NotesL"];
    std::string& DurationL = ini["Song"]["DurationL"];
    std::string& StartL = ini["Song"]["StartL"];
    std::string& StopL = ini["Song"]["StopL"];
    std::vector<std::string> NoteL = explode(NotesL, ',');
    std::vector<std::string> DurL = explode(DurationL, ',');
    std::vector<std::string> StrtL = explode(StartL, ',');
    std::vector<std::string> StpL = explode(StopL, ',');
    
    */

    std::vector<std::string> NoteR = explode(NotesR, ',');
    std::vector<std::string> DurR = explode(DurationR, ',');
    std::vector<std::string> StrtR = explode(StartR, ',');
    std::vector<std::string> StpR = explode(StopR, ',');


    


    SetConsoleCtrlHandler(CtrlHandler, TRUE);
    int i = 0;
    bool bstart = false;
    auto start = std::chrono::system_clock::now();
    /*Play on the second speaker using another thread*/
   /* std::thread Speaker(ExtSpeaker,start, NoteL, DurL, StrtL, StpL);*/
    while (i < NoteR.size())
    {   
      
        std::chrono::duration<double> elapsed_seconds = std::chrono::system_clock::now() - start;
        if ((elapsed_seconds).count() >= stod(StrtR[i]))
        {

           
            beep(static_cast<int>(stod(NoteR[i])), static_cast<int>(stod(DurR[i])*1000));
            std::cout << "Freq: " << NoteR[i] << " Duration: " << DurR[i] << " Start: " << StrtR[i] << std::endl;
            i++;
        }

        
    }
   
        
     
    //Speaker.join();
    std::cout << "Finished!\n";
    system("pause");
}


