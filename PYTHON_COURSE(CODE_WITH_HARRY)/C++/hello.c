#include <windows.h>
#include <stdio.h>

void displayAttributes(DWORD attributes) {
    if (attributes & FILE_ATTRIBUTE_DIRECTORY) {
        printf("Directory ");
    }
    if (attributes & FILE_ATTRIBUTE_READONLY) {
        printf("Read-only ");
    }
    if (attributes & FILE_ATTRIBUTE_HIDDEN) {
        printf("Hidden ");
    }
    if (attributes & FILE_ATTRIBUTE_ARCHIVE) {
        printf("Archive ");
    }
    printf("\n");
}

int main() {
    char dirPath[MAX_PATH];
    printf("Enter the path of the directory: ");
    fgets(dirPath, MAX_PATH, stdin);

    size_t len = strlen(dirPath);
    if (len > 0 && dirPath[len - 1] == '\n') {
        dirPath[len - 1] = '\0';
    }

    strcat(dirPath, "\\*");

    WIN32_FIND_DATA findData;
    HANDLE hFind = FindFirstFile(dirPath, &findData);

    if (hFind == INVALID_HANDLE_VALUE) {
        printf("Error: Directory not found or access denied.\n");
        return 1;
    }

    int fileCount = 0, dirCount = 0;
    printf("\n%-30s %-10s %-20s %-20s\n", "Name", "Size (bytes)", "Creation Date", "Attributes");
    printf("------------------------------------------------------------------------------\n");

    do {
        SYSTEMTIME st;
        FileTimeToSystemTime(&findData.ftCreationTime, &st);
        printf("%-30s %-10llu %02d-%02d-%d %02d:%02d:%02d ",
               findData.cFileName,
               ((unsigned long long)findData.nFileSizeHigh << 32) + findData.nFileSizeLow,
               st.wDay, st.wMonth, st.wYear, st.wHour, st.wMinute, st.wSecond);

        displayAttributes(findData.dwFileAttributes);

        if (findData.dwFileAttributes & FILE_ATTRIBUTE_DIRECTORY) {
            dirCount++;
        } else {
            fileCount++;
        }
    } while (FindNextFile(hFind, &findData) != 0);

    FindClose(hFind);

    printf("\nSummary:\nTotal Files: %d\nTotal Directories: %d\n", fileCount, dirCount);
    return 0;
}
