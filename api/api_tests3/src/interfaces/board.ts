export interface BoardResponse {
  id: string;
  name: string;
  desc: string;
  descData: null;
  closed: boolean;
  idOrganization: string;
  idEnterprise: null;
  pinned: boolean;
  url: string;
  shortUrl: string;
  prefs: {
    permissionLevel: string;
    hideVotes: boolean;
    voting: string;
    comments: string;
    invitations: string;
    selfJoin: boolean;
    cardCovers: boolean;
    cardCounts: boolean;
    isTemplate: boolean;
    cardAging: string;
    calendarFeedEnabled: boolean;
    hiddenPluginBoardButtons: unknown[];
    switcherViews: [
      {
        viewType: string;
        enabled: boolean;
      },
      {
        viewType: string;
        enabled: boolean;
      },
      {
        viewType: string;
        enabled: boolean;
      },
      {
        viewType: string;
        enabled: boolean;
      },
      {
        viewType: string;
        enabled: boolean;
      },
      {
        viewType: string;
        enabled: boolean;
      },
    ];
    background: string;
    backgroundColor: string;
    backgroundImage: null;
    backgroundTile: boolean;
    backgroundBrightness: string;
    sharedSourceUrl: null;
    backgroundImageScaled: null;
    backgroundBottomColor: string;
    backgroundTopColor: string;
    canBePublic: boolean;
    canBeEnterprise: boolean;
    canBeOrg: boolean;
    canBePrivate: boolean;
    canInvite: boolean;
  };
  labelNames: {
    green: string;
    yellow: string;
    orange: string;
    red: string;
    purple: string;
    blue: string;
    sky: string;
    lime: string;
    pink: string;
    black: string;
    green_dark: string;
    yellow_dark: string;
    orange_dark: string;
    red_dark: string;
    purple_dark: string;
    blue_dark: string;
    sky_dark: string;
    lime_dark: string;
    pink_dark: string;
    black_dark: string;
    green_light: string;
    yellow_light: string;
    orange_light: string;
    red_light: string;
    purple_light: string;
    blue_light: string;
    sky_light: string;
    lime_light: string;
    pink_light: string;
    black_light: string;
  };
}
