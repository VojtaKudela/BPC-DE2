
// CPU frequency in Hz required for UART_BAUD_SELECT
#ifndef F_CPU
# define F_CPU 16000000  
#endif

// RTC Definitions
#define RTC_ADR 0x68
#define RTC_SEC_MEM 0x00
#define RTC_MIN_MEM 0x01
#define RTC_HOUR_MEM 0x02
#define RTC_DAY_MEM 0x03
#define RTC_DATE_MEM 0x04
#define RTC_MONTH_MEM 0x05
#define RTC_YEAR_MEM 0x06

// DHT Sensor Definitions
#define DHT_ADR 0x5c
#define DHT_HUM_MEM 0
#define DHT_TEMP_MEM 2

// UART definition
#define BAUDRATE 9600

// Function declaration
void startup(void);
void write_rtc_data(void);
void read_rtc_data(void);
void read_dht_data(void);
void transmit_uart_data(void);

// Data packet, preper data to transmit
struct data_packet {
   volatile uint8_t year;
   volatile uint8_t month;
   volatile uint8_t date;
   volatile uint8_t day;
   volatile uint8_t hour;
   volatile uint8_t minute;
   volatile uint8_t second;
   volatile uint8_t hum_int;
   volatile uint8_t hum_dec;
   volatile uint8_t temp_int;
   volatile uint8_t temp_dec;
   volatile uint16_t lux;
   volatile uint16_t soil;
   volatile uint8_t mask;
} dp;

// Receive data from UART, time settings
struct rec_time {
   volatile uint8_t year;
   volatile uint8_t month;
   volatile uint8_t date;
   volatile uint8_t day;
   volatile uint8_t hour;
   volatile uint8_t minute;
   volatile uint8_t second;
} rc;

// Receive data from UART, regulation
struct rec_reg {
   volatile uint8_t temp_val;
   volatile uint8_t temp_hys;
   volatile uint8_t hum_val;
   volatile uint8_t hum_hys;
   volatile uint8_t soil_val;
   volatile uint8_t soil_hys;
   volatile uint8_t ilu_100;
   volatile uint8_t ilu_1;
} rg;