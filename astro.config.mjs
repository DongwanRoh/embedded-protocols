import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

export default defineConfig({
  integrations: [
    starlight({
      title: '🔌 Embedded Protocols Lab',
      description: '임베디드 시스템 하드웨어 통신 프로토콜 이론 정리, 실습 및 학습 후기',
      social: {
        github: 'https://github.com/DongwanRoh/embedded-protocols',
      },
      sidebar: [
        {
          label: '📋 커리큘럼 & 로드맵',
          items: [
            { label: '마스터 커리큘럼 (전체 계획서)', slug: 'curriculum' },
          ],
        },
        {
          label: '📚 프로토콜 이론 분석',
          autogenerate: { directory: 'theory' },
        },
        {
          label: '🛠️ 핸즈온 실습 랩 (Labs)',
          autogenerate: { directory: 'labs' },
        },
        {
          label: '✍️ 학습 일지 & 후기 (Notes)',
          autogenerate: { directory: 'notes' },
        },
      ],
    }),
  ],
});
