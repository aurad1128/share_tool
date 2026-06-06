# Requirements Document

## Introduction

面对面传输工具（热搜爬虫版）是一个Windows桌面应用程序，旨在为非技术用户提供简单易用的热搜数据爬取和分享功能。用户可以一键爬取微博、B站、抖音的热搜数据，并通过二维码或暗号在互联网上分享给他人，无需复杂配置或技术知识。

## Glossary

- **Application**: 面对面传输工具Windows桌面应用程序
- **User**: 使用本应用的操作者
- **Recipient**: 通过二维码或暗号接收数据的接收者
- **Hot_Search_Data**: 热搜数据，包含排名、标题、热度值
- **Crawler**: 爬虫模块，负责从目标平台抓取热搜数据
- **Weibo_Crawler**: 微博热搜爬虫
- **Bilibili_Crawler**: B站热搜爬虫
- **Douyin_Crawler**: 抖音热搜爬虫
- **Share_Code**: 分享暗号，用于数据传输的文本代码
- **QR_Code**: 二维码，用于数据传输的图形码
- **Excel_File**: Excel格式的数据文件
- **Local_Storage**: 本地计算机存储
- **Main_Page**: 应用主页面
- **Function_List_Page**: 功能列表页面
- **Crawling_Page**: 爬取进行中页面
- **Result_Page**: 结果展示页面
- **Share_Link**: 分享链接，包含数据访问信息

## Requirements

### Requirement 1: 微博热搜爬取

**User Story:** 作为用户，我想要一键爬取微博热搜数据，以便快速获取当前微博热门话题。

#### Acceptance Criteria

1. WHEN User clicks the Weibo crawler button, THE Weibo_Crawler SHALL fetch the top 10 hot search entries from Weibo
2. THE Weibo_Crawler SHALL extract ranking, title, and heat value for each entry
3. WHEN crawling is in progress, THE Application SHALL display a loading indicator on the Crawling_Page
4. WHEN crawling completes successfully, THE Application SHALL display the Hot_Search_Data on the Result_Page
5. IF crawling fails, THEN THE Application SHALL display an error message with retry option

### Requirement 2: B站热搜爬取

**User Story:** 作为用户，我想要一键爬取B站热搜数据，以便了解B站当前热门内容。

#### Acceptance Criteria

1. WHEN User clicks the Bilibili crawler button, THE Bilibili_Crawler SHALL fetch the top 10 hot search entries from Bilibili
2. THE Bilibili_Crawler SHALL extract ranking, title, and heat value for each entry
3. WHEN crawling is in progress, THE Application SHALL display a loading indicator on the Crawling_Page
4. WHEN crawling completes successfully, THE Application SHALL display the Hot_Search_Data on the Result_Page
5. IF crawling fails, THEN THE Application SHALL display an error message with retry option

### Requirement 3: 抖音热搜爬取

**User Story:** 作为用户，我想要一键爬取抖音热搜数据，以便掌握抖音平台热点趋势。

#### Acceptance Criteria

1. WHEN User clicks the Douyin crawler button, THE Douyin_Crawler SHALL fetch the top 10 hot search entries from Douyin
2. THE Douyin_Crawler SHALL extract ranking, title, and heat value for each entry
3. WHEN crawling is in progress, THE Application SHALL display a loading indicator on the Crawling_Page
4. WHEN crawling completes successfully, THE Application SHALL display the Hot_Search_Data on the Result_Page
5. IF crawling fails, THEN THE Application SHALL display an error message with retry option

### Requirement 4: 本地数据存储

**User Story:** 作为用户，我想要爬取的数据自动保存到本地，以便随时查看历史数据。

#### Acceptance Criteria

1. WHEN crawling completes successfully, THE Application SHALL save the Hot_Search_Data to Local_Storage as an Excel_File
2. THE Excel_File SHALL contain columns for ranking, title, heat value, platform name, and timestamp
3. THE Application SHALL organize Excel_Files by platform and date in a dedicated folder
4. THE Application SHALL use UTF-8 encoding to ensure proper display of Chinese characters
5. WHEN saving fails, THE Application SHALL log the error and notify the User

### Requirement 5: 数据预览显示

**User Story:** 作为用户，我想要在界面上直接看到爬取结果，以便快速确认数据内容。

#### Acceptance Criteria

1. WHEN crawling completes successfully, THE Result_Page SHALL display all 10 Hot_Search_Data entries
2. THE Result_Page SHALL show ranking, title, and heat value for each entry in a table format
3. THE Result_Page SHALL display the platform name and crawl timestamp
4. THE Application SHALL format heat values with thousand separators for readability
5. THE Result_Page SHALL support scrolling when content exceeds viewport height

### Requirement 6: 二维码生成

**User Story:** 作为用户，我想要生成二维码来分享数据，以便他人可以扫码获取。

#### Acceptance Criteria

1. WHEN crawling completes successfully, THE Application SHALL generate a QR_Code containing the Share_Link
2. THE QR_Code SHALL be displayed on the Result_Page
3. THE QR_Code SHALL be scannable by standard QR code readers
4. THE QR_Code SHALL have sufficient size and contrast for easy scanning
5. THE Application SHALL allow User to save the QR_Code as an image file

### Requirement 7: 暗号生成

**User Story:** 作为用户，我想要生成分享暗号，以便在无法扫码时通过文字分享数据。

#### Acceptance Criteria

1. WHEN crawling completes successfully, THE Application SHALL generate a Share_Code
2. THE Share_Code SHALL be 6 to 8 characters long and easy to read
3. THE Share_Code SHALL be displayed on the Result_Page alongside the QR_Code
4. THE Application SHALL provide a copy button to copy the Share_Code to clipboard
5. THE Share_Code SHALL be case-insensitive for ease of input

### Requirement 8: 分享链接有效期

**User Story:** 作为用户，我想要分享链接有1小时有效期，以便控制数据访问时限。

#### Acceptance Criteria

1. WHEN a Share_Link is generated, THE Application SHALL set an expiration time of 1 hour from creation
2. WHEN Recipient accesses an expired Share_Link, THE Application SHALL display an expiration message
3. THE Result_Page SHALL display the remaining valid time for the Share_Link
4. THE Application SHALL automatically clean up expired data from the server
5. THE Application SHALL allow User to regenerate a new Share_Link if expired

### Requirement 9: 互联网数据分享

**User Story:** 作为用户，我想要通过互联网分享数据，以便接收者无需在同一网络即可获取。

#### Acceptance Criteria

1. WHEN a Share_Link is generated, THE Application SHALL upload the Hot_Search_Data to a cloud service
2. WHEN Recipient accesses the Share_Link, THE Application SHALL retrieve the data from the cloud service
3. THE Application SHALL support data access from any internet-connected device
4. THE Application SHALL encrypt the data during transmission
5. IF upload fails, THEN THE Application SHALL retry up to 3 times before notifying the User

### Requirement 10: 数据接收功能

**User Story:** 作为接收者，我想要通过扫码或输入暗号获取数据，以便快速接收分享的热搜信息。

#### Acceptance Criteria

1. WHEN Recipient scans the QR_Code, THE Application SHALL navigate to the data retrieval page
2. WHEN Recipient enters a valid Share_Code, THE Application SHALL retrieve and display the Hot_Search_Data
3. THE Application SHALL display the Hot_Search_Data in the same format as the Result_Page
4. THE Application SHALL allow Recipient to download the Excel_File
5. IF the Share_Code is invalid or expired, THEN THE Application SHALL display an appropriate error message

### Requirement 11: 主页界面

**User Story:** 作为用户，我想要看到简洁友好的主页，以便快速开始使用应用。

#### Acceptance Criteria

1. WHEN the Application starts, THE Main_Page SHALL display the welcome message "欢迎使用面对面传输工具"
2. THE Main_Page SHALL display a prominent start button
3. WHEN User clicks the start button, THE Application SHALL navigate to the Function_List_Page
4. THE Main_Page SHALL use white and warm pink color scheme
5. THE Main_Page SHALL display the application logo and version number

### Requirement 12: 功能列表界面

**User Story:** 作为用户，我想要看到清晰的功能列表，以便选择要使用的爬虫。

#### Acceptance Criteria

1. THE Function_List_Page SHALL display three buttons for Weibo, Bilibili, and Douyin crawlers
2. THE Function_List_Page SHALL use icons and text labels for each crawler button
3. THE Function_List_Page SHALL maintain white and warm pink color scheme
4. THE Function_List_Page SHALL provide a back button to return to the Main_Page
5. THE Function_List_Page SHALL display a receive data button for accessing shared data

### Requirement 13: 爬取进度界面

**User Story:** 作为用户，我想要看到爬取进度提示，以便了解操作正在进行中。

#### Acceptance Criteria

1. WHEN crawling starts, THE Crawling_Page SHALL display an animated loading indicator
2. THE Crawling_Page SHALL display the platform name being crawled
3. THE Crawling_Page SHALL display a progress message such as "正在爬取数据，请稍候..."
4. THE Crawling_Page SHALL maintain white and warm pink color scheme
5. THE Crawling_Page SHALL prevent User from navigating away during crawling

### Requirement 14: 结果展示界面

**User Story:** 作为用户，我想要看到完整的结果展示，以便了解爬取成功并获取分享方式。

#### Acceptance Criteria

1. THE Result_Page SHALL display a success message at the top
2. THE Result_Page SHALL display the Hot_Search_Data table
3. THE Result_Page SHALL display the QR_Code and Share_Code side by side
4. THE Result_Page SHALL display the Share_Link expiration time
5. THE Result_Page SHALL provide buttons to return to Function_List_Page or save Excel_File

### Requirement 15: 错误处理

**User Story:** 作为用户，我想要看到清晰的错误提示，以便在出现问题时知道如何处理。

#### Acceptance Criteria

1. WHEN an error occurs, THE Application SHALL display a user-friendly error message
2. THE Application SHALL avoid displaying technical error details to the User
3. THE Application SHALL provide actionable suggestions such as retry or check network
4. THE Application SHALL log detailed error information for debugging purposes
5. THE Application SHALL allow User to return to the previous page after an error

### Requirement 16: 无参数爬取

**User Story:** 作为小白用户，我想要无需输入任何参数即可爬取，以便简化操作流程。

#### Acceptance Criteria

1. THE Application SHALL not require User to input any parameters before crawling
2. THE Crawler SHALL use predefined default settings for all crawling operations
3. THE Application SHALL automatically handle authentication and request headers
4. THE Application SHALL automatically handle rate limiting and retry logic
5. THE Application SHALL complete the entire crawling process with a single button click

### Requirement 17: Excel文件格式

**User Story:** 作为用户，我想要数据以标准Excel格式保存，以便使用Excel或WPS打开查看。

#### Acceptance Criteria

1. THE Excel_File SHALL use .xlsx file format
2. THE Excel_File SHALL include a header row with column names in Chinese
3. THE Excel_File SHALL apply basic formatting such as bold headers and borders
4. THE Excel_File SHALL auto-adjust column widths based on content
5. THE Excel_File SHALL be compatible with Microsoft Excel 2010 and later versions

### Requirement 18: 应用窗口设计

**User Story:** 作为用户，我想要应用窗口大小适中且美观，以便舒适使用。

#### Acceptance Criteria

1. THE Application SHALL open with a default window size of 800x600 pixels
2. THE Application SHALL allow User to resize the window within minimum dimensions of 600x400 pixels
3. THE Application SHALL center the window on the screen at startup
4. THE Application SHALL remember the last window size and position
5. THE Application SHALL support maximizing but not full-screen mode

### Requirement 19: 数据安全

**User Story:** 作为用户，我想要数据传输安全可靠，以便保护隐私信息。

#### Acceptance Criteria

1. WHEN uploading data to cloud service, THE Application SHALL use HTTPS protocol
2. THE Application SHALL encrypt sensitive data before transmission
3. THE Application SHALL generate unique Share_Links that are difficult to guess
4. THE Application SHALL automatically delete expired data from cloud storage
5. THE Application SHALL not collect or store User personal information

### Requirement 20: 离线功能

**User Story:** 作为用户，我想要在无网络时仍能查看本地数据，以便随时访问历史记录。

#### Acceptance Criteria

1. WHEN network is unavailable, THE Application SHALL allow User to browse Local_Storage
2. THE Application SHALL display a list of previously saved Excel_Files
3. THE Application SHALL allow User to open Excel_Files with the default spreadsheet application
4. THE Application SHALL display a network unavailable message when attempting to crawl or share
5. THE Application SHALL cache the last successful crawl result for offline viewing
