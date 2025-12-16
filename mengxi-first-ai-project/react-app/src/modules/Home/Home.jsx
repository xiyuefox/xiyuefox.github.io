import React, { useState } from 'react';
import { calculatePregnancyProgress, getTodayString } from '../../utils/dateHelper';

const PixelCard = ({ title, children, style }) => (
  <div className="pixel-border" style={{
    padding: '20px',
    backgroundColor: '#fffef8',
    marginBottom: '20px',
    ...style
  }}>
    <h3 style={{ marginTop: 0, borderBottom: '2px solid #e0d6c2', paddingBottom: '10px' }}>{title}</h3>
    {children}
  </div>
);

const Home = () => {
  const [dueDate, setDueDate] = useState(getTodayString());
  const pregnancyProgress = calculatePregnancyProgress(dueDate);

  return (
    <div style={{ maxWidth: '600px', margin: '0 auto' }}>
      <PixelCard title="👶 孕期计算器" style={{ marginBottom: '30px' }}>
        <div style={{ marginBottom: '20px' }}>
          <label style={{ display: 'block', marginBottom: '10px', fontWeight: 'bold' }}>
            请输入预产期 (YYYY-MM-DD):
          </label>
          <input
            type="date"
            value={dueDate}
            onChange={(e) => setDueDate(e.target.value)}
            className="pixel-border"
            style={{
              padding: '10px',
              backgroundColor: '#f0e6d2',
              border: 'none'
            }}
          />
        </div>

        <div style={{ textAlign: 'center', padding: '20px 0' }}>
          <div style={{ fontSize: '48px', fontWeight: 'bold', color: '#3e3065' }}>
            {pregnancyProgress.weeks}
          </div>
          <div style={{ fontSize: '24px', color: '#6e5d91' }}>周</div>
          <div style={{ fontSize: '18px', color: '#9e8dbe', marginTop: '10px' }}>
            {pregnancyProgress.days} 天
          </div>
        </div>

        <div style={{ textAlign: 'center', color: '#999' }}>
          已怀孕 {pregnancyProgress.totalDays} 天
        </div>
      </PixelCard>
    </div>
  );
};

export default Home;