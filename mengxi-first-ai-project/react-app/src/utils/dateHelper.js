import dayjs from 'dayjs';

// 引入 weekday 插件用于处理星期
import weekday from 'dayjs/plugin/weekday';
// 引入 isoWeek 插件确保周一为一周开始
import isoWeek from 'dayjs/plugin/isoWeek';

dayjs.extend(weekday);
dayjs.extend(isoWeek);

// 假设标准孕期为 40 周 (280 天)
const PREGNANCY_DURATION_DAYS = 280;

/**
 * 根据预产期计算当前的孕周和天数
 * @param {string} dueDateString - 预产期字符串 (YYYY-MM-DD)
 * @returns {object} { weeks: number, days: number, totalDays: number }
 */
export const calculatePregnancyProgress = (dueDateString) => {
  if (!dueDateString) return { weeks: 0, days: 0, totalDays: 0 };

  const dueDate = dayjs(dueDateString);
  const today = dayjs();
  // 计算最后一次月经日期 (LMP) = 预产期 - 280天
  const lmpDate = dueDate.subtract(PREGNANCY_DURATION_DAYS, 'day');

  // 计算从 LMP 到今天总共过了多少天
  const totalDaysPassed = today.diff(lmpDate, 'day');

  if (totalDaysPassed < 0) {
      // 还没怀孕或预产期设置错误
      return { weeks: 0, days: 0, totalDays: 0 };
  }

  const weeks = Math.floor(totalDaysPassed / 7);
  const days = totalDaysPassed % 7;

  return { weeks, days, totalDays: totalDaysPassed };
};

/**
 * 获取今日日期字符串 (YYYY-MM-DD)
 */
export const getTodayString = () => {
    return dayjs().format('YYYY-MM-DD');
};

/**
 * 获取当前日期所在周的所有日期对象数组 (周一到周日)
 * @returns {dayjs.Dayjs[]}
 */
export const getCurrentWeekDays = () => {
    const today = dayjs();
    const startOfWeek = today.startOf('isoWeek'); // 设置周一为开始
    const weekDays = [];
    for (let i = 0; i < 7; i++) {
        weekDays.push(startOfWeek.add(i, 'day'));
    }
    return weekDays;
};

/**
 * 格式化日期用于显示 (如 "周一 10.21")
 * @param {dayjs.Dayjs} date
 * @returns {string}
 */
export const formatDateForDisplay = (date) => {
    const weekMap = ['周日', '周一', '周二', '周三', '周四', '周五', '周六'];
    return `${weekMap[date.day()]} ${date.format('MM.DD')}`;
};

/**
 * 格式化日期作为存储 Key (如 "YYYY-MM-DD")
 * @param {dayjs.Dayjs} date
 * @returns {string}
 */
export const formatDateForKey = (date) => {
    return date.format('YYYY-MM-DD');
};

/**
 * 判断日期是否是今天
 * @param {dayjs.Dayjs} date
 * @returns {boolean}
 */
export const isToday = (date) => {
    return date.isSame(dayjs(), 'day');
};