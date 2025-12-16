import React, { useState } from 'react';

// 简单的像素风弹窗组件
const MealEditModal = ({ isOpen, onClose, onSave, mealType, initialValue, dateStr }) => {
  const [inputValue, setInputValue] = useState(initialValue || '');

  if (!isOpen) return null;

  const handleSave = () => {
    onSave(mealType, inputValue);
    onClose();
  };

  // 像素风遮罩层样式
  const overlayStyle = {
    position: 'fixed',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    backgroundColor: 'rgba(62, 48, 101, 0.7)', // 深紫色半透明
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 1000,
  };

  // 像素风弹窗内容样式
  const modalStyle = {
    backgroundColor: '#fffef8',
    padding: '20px',
    width: '90%',
    maxWidth: '400px',
    boxShadow: '4px 4px 0 0 rgba(62, 48, 101, 0.5)',
  };

  return (
    <div style={overlayStyle} onClick={onClose}>
      {/* 点击内容区域不关闭 */}
      <div className="pixel-border" style={modalStyle} onClick={(e) => e.stopPropagation()}>
        <h3 style={{ marginTop: 0, textAlign: 'center' }}>
          编辑{mealType === 'breakfast' ? '早餐' : mealType === 'lunch' ? '午餐' : '晚餐'}
          <br/>
          <span style={{ fontSize: '0.8em', fontWeight: 'normal' }}>({dateStr})</span>
        </h3>

        {/* 像素风输入框 */}
        <textarea
          className="pixel-border"
          style={{
            width: '100%',
            height: '100px',
            padding: '10px',
            backgroundColor: '#f0e6d2',
            resize: 'none',
            boxSizing: 'border-box',
            marginBottom: '20px',
            fontFamily: 'inherit',
          }}
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
          placeholder="请输入菜品内容..."
        />

        <div style={{ display: 'flex', justifyContent: 'space-between' }}>
          {/* 取消按钮 */}
          <button className="pixel-border" onClick={onClose} style={{
            padding: '8px 20px',
            backgroundColor: '#f27c7c', // 柔和红
            color: 'white',
          }}>
            取消 [X]
          </button>
          {/* 保存按钮 */}
          <button className="pixel-border" onClick={handleSave} style={{
            padding: '8px 20px',
            backgroundColor: '#8cc5a3', // 薄荷绿
            color: 'white',
          }}>
            保存 [✓]
          </button>
        </div>
      </div>
    </div>
  );
};

export default MealEditModal;