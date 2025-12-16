/**
 * 从本地存储获取数据
 * @param {string} key - 存储键名
 * @returns {Promise<any|null>} 存储的数据或 null
 */
export const getData = async (key) => {
  try {
    const data = localStorage.getItem(key);
    return data ? JSON.parse(data) : null;
  } catch (error) {
    console.error('Error getting data:', error);
    return null;
  }
};

/**
 * 将数据保存到本地存储
 * @param {string} key - 存储键名
 * @param {any} data - 要存储的数据
 * @returns {Promise<boolean>} 是否保存成功
 */
export const setData = async (key, data) => {
  try {
    localStorage.setItem(key, JSON.stringify(data));
    return true;
  } catch (error) {
    console.error('Error setting data:', error);
    return false;
  }
};